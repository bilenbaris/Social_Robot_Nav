#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Transform, Point
#include <people_msgs/People.h>
from people_msgs.msg import Person, People, PositionMeasurementArray

def callback(data):
    point = None
    
    try:    
        # rospy.loginfo("I am hear")
        # print("hello")
        new_people = Person("baris", Point(data.detections[0].x, data.detections[0].y, 0),Point(0,0,0), 0.0, [],[])
        pub = rospy.Publisher('people', People, queue_size=100)
        rospy.init_node('peoplePublisherNode', anonymous=True)
        converted_people = People()
        converted_people.header = data.header
        converted_people.header.frame_id = "odom"

        converted_people.people.append(new_people)
        # print("dasfdas", converted_people)
        pub.publish(converted_people)
    
    except:
        point = Point(0,0,0)    
    
   
    
def listener():
    #we are sending old value according to rate(20)
    rospy.init_node('people', anonymous=True)
    rate = rospy.Rate(300)
    while True:
        rospy.Subscriber("/leg_tracker_measurements", PositionMeasurementArray, callback)
        rate.sleep()
        # spin() simply keeps python from exiting until this node is stopped
    # rospy.spin()

if __name__ == '__main__':
    listener()
    posPublisher()