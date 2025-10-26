#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
from time import sleep

ROS_Frames = None
Bridge=CvBridge()

def callback(data):
    global ROS_Frames
    ROS_Frames=Bridge.imgmsg_to_cv2(data)

def process():
    global ROS_Frames
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        if ROS_Frames is not None:
            height, width = ROS_Frames.shape

            
            square_size = 100  
            start_point = (width // 2 - square_size // 2, height // 2 - square_size // 2)
            end_point = (start_point[0] + square_size, start_point[1] + square_size)

            
            color = (0, 128, 0) 
            thickness = 3

            
            image = cv2.rectangle(ROS_Frames.copy(), start_point, end_point, color, thickness)
        
            cv2.imshow("camera",image)
            print("Receiving camera data") 
            if cv2.waitKey(1) & 0xff == ord('q'):  
                break
            rate.sleep()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    rospy.init_node('square_in_frame',anonymous=True)
    rospy.Subscriber('/camera_frames',Image,callback)
    sleep(1)
    process()