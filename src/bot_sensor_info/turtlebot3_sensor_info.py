#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
import math

#find the max range and its index
def min_range_index(ranges):
    ranges = [x for x in ranges if not math.isnan(x)]
    return (min(ranges), ranges.index(min(ranges)) )

#find the max range 
def max_range_index(ranges):
    ranges = [x for x in ranges if not math.isnan(x)]
    return (max(ranges), ranges.index(max(ranges)) )

#find the average range
def average_range(ranges):
    ranges = [x for x in ranges if not math.isnan(x)]
    return ( sum(ranges) / float(len(ranges)) )

def average_between_indices(ranges, i, j):
    ranges = [x for x in ranges if not math.isnan(x)]
    slice_of_array = ranges[i: j+1]
    return ( sum(slice_of_array) / float(len(slice_of_array)) )

def scan_callback(data):
    min_value, min_index = min_range_index(data.ranges)
    print("The min range value is: ", min_value)
    print("The min range index is: ", min_index)

    max_value, max_index = max_range_index(data.ranges)
    print("The max range value is: ", max_value)
    print("The max range index is: ", max_index)

    average_value = average_range(data.ranges)
    print("The average range value is: ", average_value)

    average2 = average_between_indices(data.ranges, 2, 7)
    print("The average range between 2 indeces is: ", average2)


if __name__ == "__main__":
    rospy.init_node("scan_node", anonymous=True)

    rospy.Subscriber("scan", LaserScan, scan_callback)

    rospy.spin()