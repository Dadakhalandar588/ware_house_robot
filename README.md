# 🤖 ROS 2 Warehouse Robot Simulation & Navigation

A mobile robotics project using **ROS 2 Jazzy, Gazebo, and Nav2** to explore warehouse simulation, robot description, localization, and autonomous navigation.



---

## 📌 Overview

This project brings together the core components of a simulated warehouse robot using ROS 2.

### ✨ Key Components

- 🏭 **Warehouse Simulation** — A warehouse environment defined in Gazebo SDF.
- 🤖 **Robot Description** — Robot models using URDF and Xacro.
- 🗺️ **Warehouse Map** — A saved occupancy-grid map for map-based localization.
- 📍 **Localization** — AMCL and EKF configuration.
- 🧭 **Autonomous Navigation** — Nav2 planner, controller, and costmap configurations.
- ⚙️ **SLAM** — Configuration files for mapping-related functionality.

## 🛠️ Technology Stack

| Technology         | Purpose                          |
| ------------------ | -------------------------------- |
| ROS 2 Jazzy        | Robot middleware                 |
| Gazebo             | Robot and environment simulation |
| URDF / Xacro       | Robot description                |
| Nav2               | Navigation framework             |
| AMCL               | Map-based localization           |
| robot_localization | State estimation                 |
| Python             | ROS 2 package and launch support |

## 📂 Project Structure

```text
ware_house_robot/
├── .gitignore
├── README.md
└── src/
    └── my_robot_controller/
        ├── config/
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
        └── setup.py
```

## ⚙️ Requirements

- Ubuntu with ROS 2 Jazzy
- Gazebo and the required ROS–Gazebo integration packages
- Nav2
- robot_state_publisher
- robot_localization
- Dependencies declared by the ROS 2 package

## 🚀 Installation

### 1. Clone the repository

```bash
git clone git@github.com:Dadakhalandar588/ware_house_robot.git
cd ware_house_robot
```

### 2. Source ROS 2

```bash
source /opt/ros/jazzy/setup.bash
```

### 3. Install dependencies

```bash
rosdep install --from-paths src --ignore-src -r -y
```

### 4. Build the workspace

```bash
colcon build --packages-select my_robot_controller
source install/setup.bash
```

## ▶️ Launch the Project

Run commands from the workspace root after sourcing ROS 2 and building the package.

### Start the Gazebo simulation

```bash
ros2 launch my_robot_controller gazebo.launch.py
```

### Start localization and navigation

Open another terminal and source the ROS 2 and workspace environments:

```bash
source /opt/ros/jazzy/setup.bash
source ~/ros2workspace/install/setup.bash
ros2 launch my_robot_controller movment.launch.py
```

> **Note:** The simulation, sensor topics, transforms, map, and navigation configuration must be compatible. Verify the runtime behavior before considering the complete navigation pipeline validated.

## 🗺️ Configuration

The `config/` directory contains configuration files for:

- AMCL localization
- EKF state estimation
- Nav2 planning and control
- Local and global costmaps
- Behavior-tree navigation
- SLAM

The `warehouse_map/` directory contains the saved occupancy-grid map and its YAML metadata.

## 📈 Project Status

- [x] ROS 2 package builds successfully.
- [x] Robot description and warehouse world files included.
- [x] Saved warehouse map included.
- [x] Localization and navigation configuration files included.
- [x] Verify the Gazebo simulation at runtime.
- [x] Verify end-to-end autonomous navigation.

## 👨‍💻 Author

**Shaik Khalandar**
AI & Robotics Undergraduate | Robotics & AI

