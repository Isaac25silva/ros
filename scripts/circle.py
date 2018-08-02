#!/usr/bin/env python

# Atividade - Este foi o codigo utilizado para controlar a tartaruga no turtle_sim
# Voce deve alterar esse codigo para que ele funcione com o youbot 


import rospy
from geometry_msgs.msg import Twist

def turtle_circle():
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rospy.init_node('robot_circle', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    rate.sleep()

    vel = Twist()
    time = rospy.get_time()
    while (rospy.get_time() - time <= 6):
        print (rospy.get_time() - time)
        vel.linear.x = 0.5
        vel.angular.z = 0.2
        pub.publish(vel)
        rate.sleep()
    vel.linear.x = 0.0
    vel.angular.z = 0.0
    pub.publish(vel)

if __name__ == '__main__':
    try:
        turtle_circle()
    except rospy.ROSInterruptException:
        pass
