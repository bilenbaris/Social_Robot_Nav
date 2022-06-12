#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Transform, Point
#include <people_msgs/People.h>
from people_msgs.msg import Person, People, PositionMeasurementArray

def callback(data):
    point = None
    
    try:    
        new_person = Person("baris", Point(data.people[0].pos.x, data.people[0].pos.y, 0),Point(0,0,0), 0.0, [],[])
        converted_people = People()
        converted_people.header = data.header
        converted_people.header.frame_id = "map"
        converted_people.people.append(new_person)
        pub.publish(converted_people)
    
    except:
        point = Point(0,0,0)    
    


if __name__ == '__main__':
    rospy.init_node('peoplePublisher', anonymous=True)
    pub = rospy.Publisher('/people', People, queue_size=100)
    rate = rospy.Rate(300)
    rospy.Subscriber("/leg_tracker_measurements", PositionMeasurementArray, callback)
    rospy.spin()