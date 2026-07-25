#!/usr/bin/env python3
import rclpy 
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import TransformStamped
import tf2_ros
from my_robot_controller import utli

class multi_broadcaster(Node):
    def __init__(self):
        super().__init__("multi_broadcaster")
        self.broadcaster = tf2_ros.TransformBroadcaster(self)
        
        # Subscribe to BOTH turtles
        self.sub1 = self.create_subscription(
            Pose, '/turtle1/pose', self.callback1, 10
        )
        self.sub2 = self.create_subscription(
            Pose, '/turtle2/pose', self.callback2, 10
        )
    
    def callback1(self, msg: Pose):
        # Broadcast Turtle 1
        t = TransformStamped()
        t.header.stamp = self.get_clock().now().to_msg()
        t.header.frame_id = "world"
        t.child_frame_id = "turtle1"
        t.transform.translation.x = msg.x
        t.transform.translation.y = msg.y
        t.transform.translation.z = 0.0
        quad = utli.euler_to_quaternion(0, 0, msg.theta)
        t.transform.rotation.x = quad[0]
        t.transform.rotation.y = quad[1]
        t.transform.rotation.z = quad[2]
        t.transform.rotation.w = quad[3]
        self.broadcaster.sendTransform(t)
    
    def callback2(self, msg: Pose):
        # Broadcast Turtle 2
        t = TransformStamped()
        t.header.stamp = self.get_clock().now().to_msg()
        t.header.frame_id = "world"
        t.child_frame_id = "turtle2"
        t.transform.translation.x = msg.x
        t.transform.translation.y = msg.y
        t.transform.translation.z = 0.0
        quad = utli.euler_to_quaternion(0, 0, msg.theta)
        t.transform.rotation.x = quad[0]
        t.transform.rotation.y = quad[1]
        t.transform.rotation.z = quad[2]
        t.transform.rotation.w = quad[3]
        self.broadcaster.sendTransform(t)

def main(args=None):
    rclpy.init(args=args)
    node = multi_broadcaster()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()