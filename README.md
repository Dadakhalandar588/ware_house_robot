ROS 2 Warehouse Robot Simulation and Navigation
A ROS 2 project for simulating a mobile robot in a warehouse environment using Gazebo, with robot description files, a saved warehouse map, localization, and Nav2 navigation components.
Project Overview
This project brings together:
- ROS 2 Jazzy for robot software and communication.
- Gazebo for the warehouse simulation.
- URDF and Xacro for the robot description.
- SLAM configuration for mapping-related functionality.
- AMCL and EKF configuration for localization and state estimation.
- Nav2 configuration for path planning, control, and navigation.
- Saved warehouse map for map-based localization and navigation.
Repository Structure
my_robot_controller/
├── config/
│   ├── amcl.yaml
│   ├── behaviour_server.yaml
│   ├── bt.xml
│   ├── bt.yaml
│   ├── controller.yaml
│   ├── ekf.yaml
│   ├── globalcostmap.yaml
│   ├── lifecycle.yaml
│   ├── localcostmap.yaml
│   ├── planner.yaml
│   └── slam_params.yaml
├── gazebo_workspaces/
│   └── warehouse.sdf
├── launch/
│   ├── gazebo.launch.py
│   └── movment.launch.py
├── my_robot_controller/
│   └── __init__.py
├── urdf/
│   ├── slam.urdf
│   └── slam.urdf.xacro
├── warehouse_map/
│   ├── warehouse_map.pgm
│   └── warehouse_map.yaml
├── package.xml
├── setup.cfg
├── setup.py
├── .gitignore
└── README.md
Requirements
- Ubuntu with ROS 2 Jazzy installed.
- Gazebo and the ROS–Gazebo integration packages required by the launch files.
- Nav2 packages.
- robot_state_publisher.
- robot_localization.
- Any additional dependencies declared in package.xml or required by the robot description.
Build
Source ROS 2:
source /opt/ros/jazzy/setup.bash
Navigate to your workspace root and build the package:
cd ~/ros2workspace
colcon build --packages-select my_robot_controller
source install/setup.bash
Launch
Start the Gazebo simulation
ros2 launch my_robot_controller gazebo.launch.py
Start localization and navigation
ros2 launch my_robot_controller movment.launch.py
Launch the simulation first when required. Ensure that the robot, sensor topics, transforms, map, and navigation configuration are available before starting navigation.
Configuration
The config/ directory contains parameters for localization, state estimation, planning, controller behavior, costmaps, behavior-tree navigation, and SLAM.

The warehouse_map/ directory contains the saved occupancy-grid map and its YAML metadata.
Project Status
The ROS 2 package builds successfully with colcon build --packages-select my_robot_controller.

Gazebo simulation and Nav2 runtime behavior should be tested on the target ROS 2 installation before considering the complete navigation pipeline validated.
