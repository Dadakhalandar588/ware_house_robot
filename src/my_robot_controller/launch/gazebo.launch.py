import os
import subprocess

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

from launch_ros.actions import Node
from launch.actions import TimerAction


def generate_launch_description():

    package_path = get_package_share_directory("my_robot_controller")



    urdf_file = os.path.join(
        package_path,
        "urdf",
        "slam.urdf"
    )
    sdf_file = os.path.join(
        package_path,
        "urdf",
        "slam.sdf"
    )

    # --------------------------------------------------------
    # Convert URDF -> SDF automatically
    # --------------------------------------------------------

    subprocess.run(
        ["gz", "sdf", "-p", urdf_file],
        stdout=open(sdf_file, "w"),
        check=True
    )


    with open(urdf_file, "r") as file:
        robot_description = file.read()

  

    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory("ros_gz_sim"),
                "launch",
                "gz_sim.launch.py"
            )
        ),
        launch_arguments={
            "gz_args": ["-r ", os.path.join(
                package_path,
                "gazebo_workspaces",
                "warehouse.sdf"
    )]
}.items()
    )



    robot_state_publisher = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        output="screen",
        parameters=[
            {
                "robot_description": robot_description
            }
        ]
    )


    spawn_robot = TimerAction(
            period=5.0,
            actions=[
            Node(
                package="ros_gz_sim",
                executable="create",
                output="screen",
                arguments=[
                "-name", "slam_robot",
                "-file", sdf_file,
                "-x", "0.0",
                "-y", "0.5",
                "-z", "0.015"
            ]
        )
        ]
    )
    bridge = Node(
        package="ros_gz_bridge",
        executable="parameter_bridge",
        arguments=[
           "/world/ware_house/model/slam_robot/link/sliding_link/sensor/camera_sensor/camera_info@sensor_msgs/msg/CameraInfo[gz.msgs.CameraInfo",
           "/world/ware_house/model/slam_robot/link/sliding_link/sensor/camera_sensor/image@sensor_msgs/msg/Image[gz.msgs.Image",
           "/scan@sensor_msgs/msg/LaserScan[gz.msgs.LaserScan",
            "/imu@sensor_msgs/msg/Imu[gz.msgs.IMU",
            "/cmd_vel@geometry_msgs/msg/Twist]gz.msgs.Twist"


        ]
        
    )

    return LaunchDescription([
        gazebo,
        robot_state_publisher,
        spawn_robot,
        bridge
    ])