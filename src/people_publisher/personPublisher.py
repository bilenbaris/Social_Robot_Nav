#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Transform, Point
from people_msgs.msg import Person, People, PositionMeasurementArray


def talker():

    pub = rospy.Publisher('/people', People, queue_size=10)

    rospy.init_node('person1', anonymous=True)

    # rate = rospy.Rate(1)

    while not rospy.is_shutdown():

        #(103,100),(),(),()
        new_person1 = Person("baris", Point(97, 97.42, 0),Point(0,0,0), 0.0, [],[])
        # new_person2 = Person("baris2", Point(104, 100.2, 0),Point(0,0,0), 0.0, [],[])
        # new_person3 = Person("baris3", Point(97.3, 104, 0),Point(0,0,0), 0.0, [],[])
        # new_person4 = Person("baris4", Point(104.3, 106.8, 0),Point(0,0,0), 0.0, [],[])
        # new_person5 = Person("baris5", Point(97, 105.7, 0),Point(0,0,0), 0.0, [],[])

        converted_people1 = People()
        converted_people1.header.frame_id = "map"
        converted_people1.people.append(new_person1)
        # converted_people1.people.append(new_person2)
        # converted_people1.people.append(new_person3)
        # converted_people1.people.append(new_person4)
        # converted_people1.people.append(new_person5)

        pub.publish(converted_people1)
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass