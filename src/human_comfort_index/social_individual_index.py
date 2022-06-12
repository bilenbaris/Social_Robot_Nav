#!/usr/bin/env python

import rospy
import message_filters
from people_msgs.msg import People, PositionMeasurementArray
from geometry_msgs.msg import PoseWithCovarianceStamped
from std_msgs.msg import Float32
import math

# def callback(people, pose):
#     print("Hello")
#     people_x = people.people[0].position.x
#     people_y = people.people[0].position.y

#     pose_x = pose.pose.pose.position.x
#     pose_y = pose.pose.pose.position.y

#     deneme = math.sqrt((people_x-pose_x)**2+(people_y-pose_y)**2)
#     distance_publisher.publish(deneme)

# if __name__ == '__main__':
    
#     rospy.init_node('social_individual_index')
#     distance_publisher = rospy.Publisher('sii_distance', Float32, queue_size=10)

#     ###---Synchron---###
#     people_sub = message_filters.Subscriber('/people', People)
#     pose_sub = message_filters.Subscriber('/amcl_pose', PoseWithCovarianceStamped)
#     ts = message_filters.ApproximateTimeSynchronizer([people_sub, pose_sub], queue_size=10, slop=1)
#     ts.registerCallback(callback)
#     rospy.spin()

#ododm ve baselikn denenmeli çalışığ çaşlışmadığını anlamak için (baselink tf için yenisini buşl)

def people_callback(people):
    callback_args = people
    # people_x = people.people[0].pos.x
    # people_y = people.people[0].pos.y

    # print("Human")
    # print(people_x, people_y)
    rospy.Subscriber('/amcl_pose', PoseWithCovarianceStamped, pose_callback, callback_args)


def pose_callback(pose, args):
    pose_x = pose.pose.pose.position.x
    pose_y = pose.pose.pose.position.y

    people_x = args.people[0].pos.x
    people_y = args.people[0].pos.y

    # print("Human")
    # print(people_x, people_y)

    # print("Robot")
    # print(pose_x, pose_y)

    distance = math.sqrt((people_x-pose_x)**2+(people_y-pose_y)**2)
    closeness = 1 / distance
    # print("Distance:",closeness)
    distance_publisher.publish(closeness)


if __name__ == '__main__':
    
    rospy.init_node('social_individual_index')
    distance_publisher = rospy.Publisher('sii_distance', Float32, queue_size=10)

    
    rospy.Subscriber("/leg_tracker_measurements", PositionMeasurementArray, people_callback)
    
    rospy.spin()