#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
from turtlesim.msg import Pose

def poseCallBackFunc(msg):
    rospy.loginfo("TUrtle pose: x:%0.6f, y:%0.6f", msg.x, msg.y)

def turtle_pose_sucscriber():
    rospy.init_node('turtle_pose_sucscriber', anonymous=True)

    rospy.Subscriber("/turtle1/pose", Pose, poseCallBackFunc)

    rospy.spin()


if __name__ == '__main__':
    turtle_pose_sucscriber()