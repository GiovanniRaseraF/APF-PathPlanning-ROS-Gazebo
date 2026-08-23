SHELL := /bin/bash

dep:
	rosdep install -r -y --from-paths . --ignore-src --rosdistro $$ROS_DISTRO
do:
	colcon build
run:
	source install/setup.bash && ros2 launch sjtu_drone_bringup sjtu_drone_bringup.launch.py
p:
	git add . && git commit && git push