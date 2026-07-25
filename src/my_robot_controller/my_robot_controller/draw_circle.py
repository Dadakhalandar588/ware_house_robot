#! usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from rclpy.parameter import Parameter
class DrawCircle(Node):
    def __init__(self):
        super().__init__('draw_circle')
        self.declare_parameter("linear_speed",1.0)
        self.declare_parameter("angular_speed",0.3)
        self.get_logger().info('Draw Circle Node has been started')
        self.create_timer(0.5,self.publisher_callback)
        self.cmd_vel_publisher = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
    def publisher_callback(self):
        msg = Twist()
        linear_speed = self.get_parameter("linear_speed").value
        angular_speed = self.get_parameter("angular_speed").value
        msg.linear.x = linear_speed
        msg.angular.z = angular_speed
        self.cmd_vel_publisher.publish(msg) 
def main(args=None):
    rclpy.init(args=args)
    node = DrawCircle()
    rclpy.spin(node)
    rclpy.shutdown()

