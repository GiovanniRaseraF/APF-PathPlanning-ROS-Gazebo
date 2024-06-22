# Author: Giovanni Rasera

import rclpy

from rclpy.node import Node
import sys
import termios
import tty

from std_msgs.msg import Empty, Bool, Int8, String
from geometry_msgs.msg import Twist, Pose, Vector3
from sensor_msgs.msg import Range, Image, Imu

# positioning
from converter_position import *
from field import *

# this is to test different types of topics
prefix = "/simple_drone/"

class APFConrolNode(Node):
    def __init__(self) -> None:
        self.pose = None
        super().__init__('apf_control')

        # Control speed
        self.cmd_vel_publisher = self.create_publisher(Twist, f'{prefix}cmd_vel', 10)

        # Drone positioning
        self.sub_gt_pose = self.create_subscription(Pose, f"{prefix}gt_pose", self.cb_gt_pose, 10)

    
    def cb_gt_pose(self, p):
        self.pose = p
        # Message Structure
        """geometry_msgs.msg.Pose(
                position=geometry_msgs.msg.Point(
                    x=-9.277429850948648, 
                    y=-0.00543712248685583, 
                    z=0.05000287573880944
                ), 
                orientation=geometry_msgs.msg.Quaternion(
                    x=1.24447577829819e-05, 
                    y=-4.13604384898043e-06, 
                    z=0.00662843250080105, 
                    w=0.9999780316139969
                )
            )
        """
        pos = p.position
        x = pos.x
        y = pos.y

        # calculate field positioning
        fx, fy = gazebo_to_python(x, y)

        print(f"fx: {fx}")
        print(f"fy: {fy}")
        
        # read speed from field
        x_speed, y_speed = get_field_power(fx, fy)

        print(f"x_speed: {x_speed}")
        print(f"y_speed: {y_speed}")

        linear_vec = Vector3()
        linear_vec.x = x_speed
        linear_vec.y = y_speed

        # Actuate
        self.publish_cmd_vel(linear_vec=linear_vec)

    # Speed write
    def publish_cmd_vel(self, linear_vec: Vector3 = Vector3(), angular_vec: Vector3 = Vector3()) -> None:
        """
        Publish a Twist message to cmd_vel topic
        """
        twist = Twist(linear=linear_vec, angular=angular_vec)
        print(twist)
        self.cmd_vel_publisher.publish(twist)

# run loop
def main(args=None):
    rclpy.init(args=args)
    apf_control_node = APFConrolNode()
    rclpy.spin(apf_control_node)
    apf_control_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
