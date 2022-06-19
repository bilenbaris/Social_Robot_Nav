# social_robot_nav
Socially Aware Robot Navigation on Ros.

This is a autonomous robot navigation project with social awareness. Robot can recognize humans and act accordingly while navigating in a known map. Also gives out Human Comfortable Safety Indice (HCSI) (https://doi.org/10.1007/s12369-016-0352-0) values of robot to measure the affectiveness of social navigation.


Few things to know about this project:
  - Done using Ros Noetic on Ubuntu 20.04,
  - Uses base_local_planner as local planner (http://wiki.ros.org/base_local_planner),
  - Uses navfn as global planner (http://wiki.ros.org/navfn),
  - Uses turtlebot3 for robot (http://wiki.ros.org/turtlebot3),
  - Uses navigation for navigation (http://wiki.ros.org/navigation),
  - Uses costmap_2d for cost map (http://wiki.ros.org/costmap_2d). Has 4 layers (Static, Inflation, Obstacle, Social) for cost map,
  - Uses social_navigation_layer for social layer  (http://wiki.ros.org/social_navigation_layers),
  - Uses people for leg detection (http://wiki.ros.org/people). leg_detection uses sensor info to guess where the legs are on the map.

You can launch the project by calling "roslaunch social_robot_nav master.launch". You can also find configuration and launch file for gmapping (http://wiki.ros.org/gmapping) in this project. 

Usefull information:
  - In .bashrc you can add this lines to make your work easier:
    - source /opt/ros/noetic/setup.bash
    - source /home/baris/catkin_ws/devel/setup.bash (Prevents you to add your workspace source everytime you open a new terminal)
    - alias masterlaunch='roslaunch guided_research master.launch' (Creating alias for launching so you don't have to write long roslaunch command everytime)
  - In rviz you can check different published topics by clicking "Add" then clicking "By Topic"
  - You can run the command "rosrun rqt_graph rqt_graph" to see the published and subscribed nodes
  - After launch of gazebo and rviz you need to set the robots position on rviz manually. It can be done by selecting "2D Pose Estimate" and then clicking on the map,
