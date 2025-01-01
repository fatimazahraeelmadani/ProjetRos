#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class StatusBroadcaster(Node):
    def _init_(self):
        super()._init_('status_broadcaster')
        self.publisher_ = self.create_publisher(String, 'robot_status', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)
        self.get_logger().info('Status Broadcaster is running.')

    def timer_callback(self):
        msg = String()
        # Remplacez par la logique pour obtenir le statut actuel du robot
        msg.data = 'Robot is operational.'
        self.publisher_.publish(msg)
        self.get_logger().info('Published status: "%s"' % msg.data)

def main(args=None):
    rclpy.init(args=args)
    status_broadcaster = StatusBroadcaster()
    rclpy.spin(status_broadcaster)
    status_broadcaster.destroy_node()
    rclpy.shutdown()

if _name_ == '_main_':
    main()