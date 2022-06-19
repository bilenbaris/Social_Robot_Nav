cmake_minimum_required(VERSION 3.0.2)
project(social_robot_nav)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
)

catkin_package(
  CATKIN_DEPENDS roscpp rospy std_msgs message_runtime
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

install(DIRECTORY launch maps
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

catkin_install_python(PROGRAMS src/people_publisher/peoplePublisher.py DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})

catkin_install_python(PROGRAMS src/people_publisher/personPublisher.py DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})

catkin_install_python(PROGRAMS src/human_comfort_index/social_individual_index.py DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})