#usr/bin/env python3
import rclpy
from rclpy.node  import Node
class first_node(Node):
    def __init__(self):
        super().__init__('node_name')
        self.counter= 0
        self.create_timer(1.0, self.timer_callback)    
    def timer_callback(self):
        self.get_logger().info('Hello World: %d' % self.counter)
        self.counter += 1
def main(args=None):
    rclpy.init(args=args)
    node = first_node()
    rclpy.spin(node)
    rclpy.shutdown()
    