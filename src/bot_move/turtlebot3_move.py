#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

def move():

    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

    rospy.init_node('move', anonymous=True)

    rate = rospy.Rate(1)

    i = 0
    while not rospy.is_shutdown():
        twist = Twist()

        if i < 10:
            twist.linear.x = 1.0
            twist.linear.y = 0.0
            twist.linear.z = 0.0

            twist.angular.x = 0.0
            twist.angular.y = 0.0
            twist.angular.z = 0.0
        else:
            twist.linear.x = 0.0
            twist.linear.y = 0.0
            twist.linear.z = 0.0

            twist.angular.x = 0.0
            twist.angular.y = 0.0
            twist.angular.z = 0.0

        i += 1
        rospy.loginfo(twist)
        pub.publish(twist)
        rate.sleep()

if __name__ == '__main__':
    try:
        move()
    except rospy.ROSInterruptException:
        pass