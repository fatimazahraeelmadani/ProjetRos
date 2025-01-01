#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan

class SensorReader(Node):
    def _init_(self):
        super()._init_('sensor_reader')
        self.publisher_ = self.create_publisher(LaserScan, '/sensor_data', 10)
        self.timer = self.create_timer(0.1, self.timer_callback)  # 10 Hz
        self.get_logger().info('Sensor Reader is running.')

    def timer_callback(self):
        scan_data = LaserScan()
        # Remplacez par la logique pour lire les données réelles du capteur LiDAR
        scan_data.header.stamp = self.get_clock().now().to_msg()
        scan_data.header.frame_id = 'laser_frame'
        # Exemple de données fictives
        scan_data.angle_min = -1.57
        scan_data.angle_max = 1.57
        scan_data.angle_increment = 0.01
        scan_data.time_increment = 0.0
        scan_data.scan_time = 0.1
        scan_data.range_min = 0.12
        scan_data.range_max = 3.5
        scan_data.ranges = [1.0] * int((scan_data.angle_max - scan_data.angle_min) / scan_data.angle_increment)
        self.publisher_.publish(scan_data)
        self.get_logger().info('Published LiDAR scan data.')

def main(args=None):
    rclpy.init(args=args)
    sensor_reader = SensorReader()
    rclpy.spin(sensor_reader)
    sensor_reader.destroy_node()
    rclpy.shutdown()

if _name_ == '_main_':
    main()