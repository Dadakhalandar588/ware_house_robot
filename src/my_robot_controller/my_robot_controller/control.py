#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from turtlesim.srv import SetPen

class create_control(Node):
    def __init__(self):
        super().__init__("control_node")

        self.__position__x = 0

        self.cmd_vel_pub = self.create_publisher(
            Twist,
            "/turtle1/cmd_vel",
            10
        )

        self.cmd_pose = self.create_subscription(
            Pose,
            "/turtle1/pose",
            self.playback,
            10
        )

    def playback(self,msg:Pose):

        cmd = Twist()

        if msg.x >= 9.0 or msg.x < 2.0 or msg.y >= 9.0 or msg.y <= 2.0:
            cmd.linear.x = 1.0
            cmd.angular.z = 0.6
        else:
            cmd.linear.x = 3.0
            cmd.angular.z = 0.0

        self.cmd_vel_pub.publish(cmd)

        if msg.x >= 5.5 and self.__position__x < 5.5:
            self.get_logger().info("the path will print in red")
            self.service(100,0,0,10,0)

        elif msg.x <= 5.5 and self.__position__x > 5.5:
            self.get_logger().info("the path will be in green")
            self.service(0,100,0,10,0)

        self.__position__x = msg.x

    def service(self,r,g,b,width,off):

        client = self.create_client(
            SetPen,
            "/turtle1/set_pen"
        )

        while not client.wait_for_service(timeout_sec=1.0):
            self.get_logger().warn(
                "waiting for the service to connect"
            )

        request = SetPen.Request()

        request.r = r
        request.g = g
        request.b = b
        request.width = width
        request.off = off

        future = client.call_async(request)

        future.add_done_callback(
            self.call_back
        )

    def call_back(self,future):

        try:
            response = future.result()

            self.get_logger().info(
                "pen updated"
            )

        except Exception as e:

            self.get_logger().error(
                f"error {e}"
            )

def main(args=None):

    rclpy.init(args=args)

    node = create_control()

    rclpy.spin(node)

    rclpy.shutdown()

if __name__ == "__main__":
    main()