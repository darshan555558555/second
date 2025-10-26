#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
from time import sleep

ROS_Frames = 0
Bridge=CvBridge()

def callback(data):
    global ROS_Frames
    ROS_Frames=Bridge.imgmsg_to_cv2(data)

def process():
    global ROS_Frames
    rate = rospy.Rate(10)
    while True:
        cv2.imshow("camera",ROS_Frames)
        print("Receiving camera data") 
        if cv2.waitKey(1) & 0xff == ord('q'):  
            break
        rate.sleep()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    rospy.init_node('camera_subscriber',anonymous=True)
    rospy.Subscriber('/camera_frames',Image,callback)
    sleep(1)
    process()