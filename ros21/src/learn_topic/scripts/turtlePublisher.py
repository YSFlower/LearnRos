#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
from geometry_msgs.msg import Twist

def turtlePublisher():

    rospy.init_node('turtle_Publisher', anonymous=True)

    turtle_vel_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        vel_msg = Twist()
        vel_msg.linear.x = 0.5
        vel_msg.angular.z = 0.2

        turtle_vel_pub.publish(vel_msg)
        rospy.loginfo("publish turtle velocity command[%0.2f m/s, %0.2f rad/s]", vel_msg.linear.x, vel_msg.angular.z)

        rate.sleep()

if __name__ == '__main__':
    try:
        turtlePublisher()
    except rospy.ROSInterruptException:
        pass