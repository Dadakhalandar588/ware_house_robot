from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument
def generate_launch_description():
    return LaunchDescription([  
        Node(
            package='my_robot_controller',
            executable='turtle2_broadcaster',
            name='turtle2_broadcaster',
            output='screen'
        ),
        Node(
            package='my_robot_controller',
            executable='turtle3_broadcaster',
            name='turtle3_broadcaster',
            output='screen'
        ),q
        Node(
            package='my_robot_controller',
            executable='turtle4_broadcaster',
            name='turtle4_broadcaster',
            output='screen'
        ),
        Node(
            package='my_robot_controller',
            executable='turtle5_broadcaster',
            name='turtle5_broadcaster',
            output='screen'
        ),
        Node(
            package='my_robot_controller',
            executable='turtle1_broadcaster',
            name='turtle1_broadcaster',
            output='screen'
        )


        ]
  )