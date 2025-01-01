#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_srvs.srv import SetBool

class CommandListener(Node):
    def _init_(self):
        super()._init_('command_listener')
        self.srv = self.create_service(SetBool, '/set_goal', self.command_callback)
        self.get_logger().info('Service "/set_goal" ready to receive commands.')

    def command_callback(self, request, response):
        if request.data:
            self.get_logger().info('Received command to START the robot.')
            # Implémentez la logique pour démarrer le robot
            response.success = True
            response.message = 'Robot started.'
        else:
            self.get_logger().info('Received command to STOP the robot.')
            # Implémentez la logique pour arrêter le robot
            response.success = True
            response.message = 'Robot stopped.'
        return response

def main(args=None):
    rclpy.init(args=args)
    command_listener = CommandListener()
    rclpy.spin(command_listener)
    command_listener.destroy_node()
    rclpy.shutdown()

if _name_ == '_main_':
    main()