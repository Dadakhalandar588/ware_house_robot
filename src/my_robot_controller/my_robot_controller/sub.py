#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
class Subscriber(Node):
    def __init__(self):
        super().__init__('subscriber')
        self.pose_subscriber = self.create_subscription(Pose, 'turtle1/pose', self.pose_callback, 10)\

    def pose_callback(self, msg: Pose):
        self.get_logger().info(f'pose:x={msg.x}, y={msg.y}, theta={msg.theta}')

def main(args=None):
    rclpy.init(args=args)
    subscriber = Subscriber()
    rclpy.spin(subscriber)
    rclpy.shutdown()