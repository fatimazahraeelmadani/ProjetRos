#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

class CollisionAvoidance(Node):
    def _init_(self):
        super()._init_('collision_avoidance')
        self.subscription = self.create_subscription(
            LaserScan,
            'scan',
            self.scan_callback,
            10)
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)
        self.safe_distance = 0.5  # Distance de sécurité en mètres

    def scan_callback(self, msg):
        # Analysez les données LaserScan pour détecter les obstacles
        min_distance = min(msg.ranges)
        if min_distance < self.safe_distance:
            # Obstacle détecté à une distance dangereuse
            self.avoid_obstacle()
        else:
            # Aucun obstacle détecté, continuez le mouvement normal
            self.continue_movement()

    def avoid_obstacle(self):
        msg = Twist()
        msg.linear.x = 0.0
        msg.angular.z = 0.5  # Tourne à gauche
        self.publisher_.publish(msg)

    def continue_movement(self):
        msg = Twist()
        msg.linear.x = 0.2  # Avance à une vitesse constante
        msg.angular.z = 0.0
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    collision_avoidance = CollisionAvoidance()
    rclpy.spin(collision_avoidance)
    collision_avoidance.destroy_node()
    rclpy.shutdown()

if _name_ == '_main_':
    main()