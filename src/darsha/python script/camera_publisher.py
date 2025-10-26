#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge

Bridge = CvBridge()
cap = cv2.VideoCapture(-1)

def initialize_camera():
    cap.set(cv2.CAP_PROP_FRAME_WIDTH,640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT,480)

    		
def Frames_Publish():
	rate = rospy.Rate(60)
	while True:
		ret,frame = cap.read()
		if ret:
			rospy.loginfo('Publish video frame')
			ros_image = Bridge.cv2_to_imgmsg(frame ,encoding = "bgr8")
			pub.publish(ros_image)
		else:
			rospy.logwarn("failled to read frame")
			rate.sleep()
		
if __name__ == '__main__':
		rospy.init_node('camera_publisher',anonymous = True)
		pub = rospy.Publisher('/camera_frames',Image,queue_size = 10)
	
		initialize_camera()

		try :
			Frames_Publish()
					
		except rospy.ROSInterruptException:
			rospy.logwarn("unable to publish")
					
		finally:
			cap.release()
				
	    		
    
