#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan, Image

class DataFusion(Node):
    def _init_(self):
        super()._init_('data_fusion')
        self.lidar_subscription = self.create_subscription(
            LaserScan,
            'lidar_scan',
            self.lidar_callback,
            10)
        self.camera_subscription = self.create_subscription(
            Image,
            'camera_image',
            self.camera_callback,
            10)
        self.get_logger().info('Data Fusion node is running.')
        self.lidar_data = None
        self.camera_data = None

    def lidar_callback(self, msg):
        self.lidar_data = msg
        self.fuse_data()

    def camera_callback(self, msg):
        self.camera_data = msg
        self.fuse_data()

    def fuse_data(self):
        if self.lidar_data and self.camera_data:
            # Implémentez la logique pour fusionner les données LiDAR et caméra
            self.get_logger().info('Fusing LiDAR and camera data.')
            # Réinitialisez les données après la fusion
            self.lidar_data = None
            self.camera_data = None

def main(args=None):
    rclpy.init(args=args)
    data_fusion = DataFusion()
    rclpy.spin(data_fusion)
    data_fusion.destroy_node()
    rclpy.shutdown()

if _name_ == '_main_':
    main()