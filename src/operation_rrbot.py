#! /usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import Float64 as Joint
from math import sin

class rrbot:
    def __init__(self):
        rospy.init_node('operation_rrbot', anonymous=True)
        self.joint1_pub = rospy.Publisher('rrbot/joint1_position_controller/command',
                                                    Joint, queue_size=1000)
        self.joint2_pub = rospy.Publisher('rrbot/joint2_position_controller/command',
                                                    Joint, queue_size=1000)
        rospy.Timer(rospy.Duration(0.1), self.timerCallback)

        data = Joint()
        data.data = 0.0
        self.joint1_pub.publish(data)
        self.joint2_pub.publish(data)
        self.cnt1 = 0
        self.cnt2 = 0


    def timerCallback(self, event):
        self.rotate_joint1()
        self.rotate_joint2()


    def rotate_joint1(self):
        self.cnt1 = self.cnt1 + 1
        data = Joint()
        r = rospy.Rate(10)

        data.data = sin(self.cnt1 / 100.0)  # 動作を決める
        self.joint1_pub.publish(data)
        r.sleep()


    def rotate_joint2(self):
        self.cnt2 = self.cnt2 + 1
        data = Joint()
        r = rospy.Rate(10)

        data.data = sin(self.cnt2 / 100.0)  # 動作を決める
        self.joint2_pub.publish(data)
        r.sleep()


if __name__ == '__main__':

    try:
        ts = rrbot()
        rospy.spin()
    except rospy.ROSInterruptException: pass
