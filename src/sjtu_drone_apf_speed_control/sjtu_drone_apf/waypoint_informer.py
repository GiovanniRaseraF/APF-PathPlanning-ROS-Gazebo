# Author: Giovanni Rasera

import rclpy

from rclpy.node import Node
import sys
import termios
import tty

from std_msgs.msg import Empty, Bool, Int8, String
from geometry_msgs.msg import Twist, Pose, Vector3
from sensor_msgs.msg import Range, Image, Imu

import json

prefix = "/simple_drone/"

# positioning
from converter_position import *

class WayPointInformer(Node):
    def __init__(self) -> None:
        super().__init__('waypoint_informer')

        # Drone positioning
        self.sub_gt_pose = self.create_subscription(Pose, f"{prefix}gt_pose", self.cb_gt_pose, 10)

        # Waypoint 
        self.current_waypoint = 0

        # read way points
        waypoints_file = open('waypoints.json')
        self.waypoints = json.load(waypoints_file)["waypoints"]
        waypoints_file.close()

    def cb_gt_pose(self, p):
        self.pose = p

        # Message Structure
        pos = p.position
        x = pos.x
        y = pos.y
    
    # calculate wich waypoint to activate
    def calculate_waypoint(self, x : float, y : float):
         
        # change interest on waypoint change
        # the calculation in this case is simple
        for w in self.waypoints:
            number = w["number"]
            goal_x = w["goal_x"]
            goal_y = w["goal_y"]
            obstacle_x =  w["obstacle_x"]
            obstacle_y = w["obstacle_y"]
            bound_min_x = w["bound_min_x"]
            bound_max_x = w["bound_max_x"]
            bound_min_y = w["bound_min_y"]
            bound_max_y = w["bound_max_y"]
