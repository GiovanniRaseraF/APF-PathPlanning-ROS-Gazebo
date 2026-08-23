SHELL := /bin/bash

.PHONY: dep do do/system do/autopilot run run/system run/autopilot system autopilot p

# Extract optional sub-command (e.g., `make do autopilot` or `make run system`)
SUBCMD := $(word 2,$(MAKECMDGOALS))

dep:
	rosdep install -r -y --from-paths . --ignore-src --rosdistro $$ROS_DISTRO

# --- Build Targets ---
do:
ifeq ($(SUBCMD),autopilot)
	colcon build --packages-select sjtu_drone_autopilot
else
	colcon build
endif

# --- Run Targets ---
run:
ifeq ($(SUBCMD),autopilot)
	source install/setup.bash && ros2 run sjtu_drone_autopilot autopilot_node
else
	source install/setup.bash && ros2 launch sjtu_drone_bringup sjtu_drone_bringup.launch.py
endif

# Catch secondary arguments so Make doesn't throw 'No rule to make target'
system autopilot:
	@:

# --- Git Helper ---
p:
	git add . && git commit && git push