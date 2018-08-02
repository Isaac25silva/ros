#!/usr/bin/env python

import rospy
import math
import tf

from geometry_msgs.msg import Twist, PoseWithCovarianceStamped, PointStamped

class Robot:
    def __init__(self):
        rospy.init_node('robot', anonymous=True)
        rate = rospy.Rate(10) # 10hz

        self.target_position = None
        self.robot_position = None
        self.robot_angle = None

        pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        rospy.Subscriber('/amcl_pose', PoseWithCovarianceStamped, self.callback_pose)
        rospy.Subscriber('/clicked_point', PointStamped, self.callback_target)    

        while not rospy.is_shutdown():
            ################## adicione seu codigo aqui ##################


            ##############################################################
	        rate.sleep() 

    def callback_pose(self,data):
	    quaternion = (
	        data.pose.pose.orientation.x,
	        data.pose.pose.orientation.y,
	        data.pose.pose.orientation.z,
	        data.pose.pose.orientation.w)
	    euler = tf.transformations.euler_from_quaternion(quaternion)
	    roll = euler[0]
	    pitch = euler[1]
	    yaw = euler[2]
        self.robot_position = data.pose.pose.position
        self.robot_angle = yaw
	    print "robot_position = " + str(self.robot_position)
	    print "robot_angle = " + str(self.robot_angle)

    def callback_target(self,data):
        self.target_position = data.point
	    print "target_position = " + str(self.target_position)

if __name__ == '__main__':
    try:
        Robot()
    except rospy.ROSInterruptException:
        pass
