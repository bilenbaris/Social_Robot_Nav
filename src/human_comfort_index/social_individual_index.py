#!/usr/bin/env python

import rospy
import message_filters
from people_msgs.msg import People, PositionMeasurementArray
from geometry_msgs.msg import PoseWithCovarianceStamped
from std_msgs.msg import Float32
import math

# def people_callback(people):
#     control_val = 0.5
#     control_publisher.publish(control_val)
#     callback_args = people

#     rospy.Subscriber('/amcl_pose', PoseWithCovarianceStamped, pose_callback, callback_args)


# def pose_callback(pose, args):
#     pose_x = pose.pose.pose.position.x
#     pose_y = pose.pose.pose.position.y

#     print(args)
#     if(args == None):
#         people_x = 0
#         people_y = 0
#     else:
#         people_x = args.people[0].pos.x
#         people_y = args.people[0].pos.y
    
#     distance_x = people_x - pose_x
#     distance_y = people_y - pose_y

#     d_c = 1.5 #Hall's proxemics

#     x = (distance_x / (math.sqrt(2) * d_c))
#     y = (distance_y / (math.sqrt(2) * d_c))
#     SII = math.exp(-1 * ((x * x) + (y * y)))
#     distance_publisher.publish(SII)



# if __name__ == '__main__':
    
#     rospy.init_node('social_individual_index')
#     distance_publisher = rospy.Publisher('sii_value', Float32, queue_size=10)
#     control_publisher = rospy.Publisher('sii_control', Float32, queue_size=10)
    

    
#     rospy.Subscriber("/leg_tracker_measurements", PositionMeasurementArray, people_callback)
    
#     rospy.spin()


#////////////////////////////////////////////////////////////////////////////////////////////////////////////
#///////////////////////////////PERSON PUBLISHED/////////////////////////////////////////////////////////////
#////////////////////////////////////////////////////////////////////////////////////////////////////////////

# def people_callback(people):
    
#     callback_args = people
#     rospy.Subscriber('/amcl_pose', PoseWithCovarianceStamped, pose_callback, callback_args)


def pose_callback(pose): #, args
    control_val = 0.5
    control_publisher.publish(control_val)
    pose_x = pose.pose.pose.position.x
    pose_y = pose.pose.pose.position.y

    people_x = 97
    people_y = 97.42
    
    distance_x = people_x - pose_x
    distance_y = people_y - pose_y

    d_c = 0.8 #Hall's proxemics

    x = (distance_x / (math.sqrt(2) * d_c))
    y = (distance_y / (math.sqrt(2) * d_c))
    SII = math.exp(-1 * ((x * x) + (y * y)))
    distance_publisher.publish(SII)


if __name__ == '__main__':
    
    rospy.init_node('social_individual_index')
    distance_publisher = rospy.Publisher('sii_value', Float32, queue_size=10)
    control_publisher = rospy.Publisher('sii_control', Float32, queue_size=10)
    
    # rospy.Subscriber("/people", People, people_callback)
    rospy.Subscriber('/amcl_pose', PoseWithCovarianceStamped, pose_callback)
    
    rospy.spin()