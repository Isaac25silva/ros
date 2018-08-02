#!/usr/bin/env python

import rospy
import math
from geometry_msgs.msg import PoseStamped, PoseWithCovarianceStamped

roadmap = [[1.57170116901,-2.37665605545],
          [1.65528392792,-9.20154762268],
          [-8.69849395752,-6.79304504395],
          [-13.0328407288,-0.753871917725],
          [-22.2800064087,-4.25865364075],
          [-22.7731685638,5.11091804504],
          [-6.94614601135,2.02960109711]]

class Robot:

    def __init__(self):
        rospy.init_node('robot', anonymous=True)
        rate = rospy.Rate(10) # 10hz
	self.pose = None

	pub = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=10)
	rospy.Subscriber('/amcl_pose', PoseWithCovarianceStamped, self.callback_pose)

        rate.sleep()
        goal = PoseStamped()
        goal.header.frame_id = 'map'
        goal.pose.orientation.w = 1.0
	goal.pose.position.x = roadmap[0][0]
        goal.pose.position.y = roadmap[0][1]
        pub.publish(goal)
        rate.sleep()

        while not rospy.is_shutdown():
            if (self.pose == None):
                continue

	    if len(roadmap) > 0:

                ################## adicione seu codigo aqui ##################


                ##############################################################

            else:
                break

    def callback_pose(self,data):
        self.pose = data.pose.pose.position

if __name__ == '__main__':
    try:
        Robot()
    except rospy.ROSInterruptException:
        pass
