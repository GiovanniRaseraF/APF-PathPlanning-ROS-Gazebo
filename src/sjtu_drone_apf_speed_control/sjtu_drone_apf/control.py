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

# positioning
from converter_position import *
from field import *

# this is to test different types of topics
prefix = "/simple_drone/"

class APFConrolNode(Node):
    def __init__(self) -> None:
        self.pose = None
        self.autonomy = False

        super().__init__('apf_control')

        # Control speed
        self.cmd_vel_publisher = self.create_publisher(Twist, f'{prefix}cmd_vel', 10)

        # Drone positioning
        self.sub_gt_pose = self.create_subscription(Pose, f"{prefix}gt_pose", self.cb_gt_pose, 10)

        # Autonomy Toggler
        self.sub_toggle_autonomy = self.create_subscription(Empty, f"{prefix}toggle_autonomy", self.cb_t_a, 10)
        self.sub_waypoint_system = self.create_subscription(String, f"{prefix}waypoint_system", self.cb_w_s, 10)

        # Waypoint 
        self.current_waypoint = 0

    # Change interest using waypoint
    def cb_w_s(self, p):
        self.calculate_waypoint(int(p.data))

    # toggle autonomy
    def cb_t_a(self, e):
        self.autonomy = not self.autonomy 

        if(not self.autonomy):
            print("Stop Drone !")
            self.publish_cmd_vel(linear_vec=Vector3())

        print(f"Autonomy: {self.autonomy}")
    
    def cb_gt_pose(self, p):
        self.pose = p

        # Message Structure
        pos = p.position
        x = pos.x
        y = pos.y

        # calculate field positioning
        fx, fy = gazebo_to_python(y, x)

        # read speed from field
        x_speed, y_speed = get_field_power(fx, fy, scale_x = 1, scale_y = 1)
        
        #print(f"fx: {y} -> {fx} -> s: {x_speed}")
        #print(f"fy: {x} -> {fy} -> s: {-y_speed}")

        linear_vec = Vector3()

        linear_vec.x = x_speed 
        linear_vec.y = -y_speed

        # Actuate
        if(self.autonomy):
            self.publish_cmd_vel(linear_vec=linear_vec)

    # Speed write
    def publish_cmd_vel(self, linear_vec: Vector3 = Vector3(), angular_vec: Vector3 = Vector3()) -> None:
        """
        Publish a Twist message to cmd_vel topic
        """
        twist = Twist(linear=linear_vec, angular=angular_vec)
        self.cmd_vel_publisher.publish(twist)
    
    # calculate wich waypoint to activate
    def calculate_waypoint(self, interest):
        # read way points
        waypoints_file = open('waypoints.json')
        waypoints = json.load(waypoints_file)["waypoints"]

        # change interest on waypoint change
        # the calculation in this case is simple
        for w in waypoints:
            number = w["number"]
            goal_x = w["goal_x"]
            goal_y = w["goal_y"]
            obstacle_x =  w["obstacle_x"]
            obstacle_y = w["obstacle_y"]
            bound_min_x = w["bound_min_x"]
            bound_max_x = w["bound_max_x"]
            bound_min_y = w["bound_min_y"]
            bound_max_y = w["bound_max_y"]

            if(number == interest):
                print(f"New Waypoint: {interest}" )
                # now we change objective !
                newBoundaries(bound_max_x, bound_min_x, bound_max_y, bound_min_y)

                # recalculate the field based on new positioning
                setNewPositioning(newgoal=np.array([goal_x, goal_y]), newobstacle=np.array([obstacle_x, obstacle_y]))
                    
                calcForceField()

# run loop
def main(args=None):
    rclpy.init(args=args)

    # create field
    calcForceField()

    # run node
    apf_control_node = APFConrolNode()
    rclpy.spin(apf_control_node)

    apf_control_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
