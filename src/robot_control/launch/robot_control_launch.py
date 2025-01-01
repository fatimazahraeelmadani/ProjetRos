#!/usr/bin/env python3
import launch
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='robot_control',
            executable='motion_controller',
            name='motion_controller',
            output='screen',
            parameters=[{'param1': 'value1'}]  # Remplacez par vos paramètres
        ),
        Node(
            package='robot_control',
            executable='sensor_reader',
            name='sensor_reader',
            output='screen',
            parameters=[{'param2': 'value2'}]  # Remplacez par vos paramètres
        ),
        Node(
            package='robot_control',
            executable='command_listener',
            name='command_listener',
            output='screen',
            parameters=[{'param3': 'value3'}]  # Remplacez par vos paramètres
        ),
    ])