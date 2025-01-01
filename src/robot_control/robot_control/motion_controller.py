#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer
from geometry_msgs.msg import Twist
from nav_msgs.action import NavigateToPose

class MotionController(Node):
    def _init_(self):
        super()._init_('motion_controller')
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        self.timer = self.create_timer(0.1, self.timer_callback)  # 10 Hz
        self._action_server = ActionServer(
            self,
            NavigateToPose,
            '/navigate_to_pose',
            self.execute_callback)
        # Initialisez les variables pour les objectifs de mouvement
        self.target_linear_velocity = 0.0
        self.target_angular_velocity = 0.0
        self.get_logger().info('Motion Controller is running.')

    def timer_callback(self):
        msg = Twist()
        msg.linear.x = self.target_linear_velocity
        msg.angular.z = self.target_angular_velocity
        self.publisher_.publish(msg)
        self.get_logger().info(f'Published velocity command: linear={self.target_linear_velocity}, angular={self.target_angular_velocity}')

    def execute_callback(self, goal_handle):
        feedback_msg = NavigateToPose.Feedback()
        # Logique pour naviguer vers la position cible
        # Exemple : ajuster les vitesses linéaire et angulaire en fonction de l'objectif
        self.target_linear_velocity = 0.5  # Exemple de vitesse linéaire
        self.target_angular_velocity = 0.1  # Exemple de vitesse angulaire
        # Mettre à jour feedback_msg avec l'état actuel
        feedback_msg.distance_remaining = 0.0  # Exemple de distance restante
        goal_handle.publish_feedback(feedback_msg)
        # Une fois terminé
        goal_handle.succeed()
        result = NavigateToPose.Result()
        return result

def main(args=None):
    rclpy.init(args=args)
    motion_controller = MotionController()
    rclpy.spin(motion_controller)
    motion_controller.destroy_node()
    rclpy.shutdown()

if _name_ == '_main_':
    main()
