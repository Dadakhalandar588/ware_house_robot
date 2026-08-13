import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import TimerAction
from launch_ros.actions import Node


def generate_launch_description():

    package_path = get_package_share_directory(
        "my_robot_controller"
    )

    # =========================================================
    # EKF
    # =========================================================

    ekf_params = os.path.join(
        package_path,
        "config",
        "ekf.yaml"
    )

    ekf = Node(
        package="robot_localization",
        executable="ekf_node",
        name="ekf_filter_node",
        output="screen",
        parameters=[
            ekf_params,
            {
                "use_sim_time": True
            }
        ]
    )

    # =========================================================
    # MAP SERVER
    # =========================================================

    saved_map = os.path.join(
        package_path,
        "warehouse_map",
        "warehouse_map.yaml"
    )

    map_server = Node(
        package="nav2_map_server",
        executable="map_server",
        name="map_server",
        output="screen",
        parameters=[
            {
                "use_sim_time": True,
                "yaml_filename": saved_map
            }
        ]
    )

    # =========================================================
    # AMCL
    # =========================================================

    amcl_params = os.path.join(
        package_path,
        "config",
        "amcl.yaml"
    )

    amcl_server = Node(
        package="nav2_amcl",
        executable="amcl",
        name="amcl",
        output="screen",
        parameters=[
            amcl_params,
            {
                "use_sim_time": True
            }
        ]
    )

    # =========================================================
    # LOCALIZATION LIFECYCLE MANAGER
    # =========================================================

    localization_lifecycle_manager = Node(
        package="nav2_lifecycle_manager",
        executable="lifecycle_manager",
        name="lifecycle_manager_localization",
        output="screen",
        parameters=[
            {
                "use_sim_time": True,
                "autostart": True,
                "node_names": [
                    "map_server",
                    "amcl"
                ]
            }
        ]
    )

    # =========================================================
    # PLANNER + GLOBAL COSTMAP
    # =========================================================

    planner_params = os.path.join(
        package_path,
        "config",
        "planner.yaml"
    )

    global_costmap_params = os.path.join(
        package_path,
        "config",
        "globalcostmap.yaml"
    )

    planner = Node(
        package="nav2_planner",
        executable="planner_server",
        name="planner_server",
        output="screen",
        parameters=[
            planner_params,
            global_costmap_params
        ]
    )

    # =========================================================
    # CONTROLLER + LOCAL COSTMAP
    # =========================================================

    controller_params = os.path.join(
        package_path,
        "config",
        "controller.yaml"
    )

    local_costmap_params = os.path.join(
        package_path,
        "config",
        "localcostmap.yaml"
    )

    controller = Node(
        package="nav2_controller",
        executable="controller_server",
        name="controller_server",
        output="screen",
        parameters=[
            controller_params,
            local_costmap_params
        ]
    )

    # =========================================================
    # BEHAVIOR SERVER
    # =========================================================

    behavior_params = os.path.join(
        package_path,
        "config",
        "behaviour_server.yaml"
    )

    behavior_server = Node(
        package="nav2_behaviors",
        executable="behavior_server",
        name="behavior_server",
        output="screen",
        parameters=[
            behavior_params
        ]
    )

    # =========================================================
    # BT NAVIGATOR
    # =========================================================

    bt_params = os.path.join(
        package_path,
        "config",
        "bt.yaml"
    )

    bt_navigator = Node(
        package="nav2_bt_navigator",
        executable="bt_navigator",
        name="bt_navigator",
        output="screen",
        parameters=[
            bt_params
        ]
    )

    # =========================================================
    # NAVIGATION LIFECYCLE MANAGER
    # Start after localization has had time to publish map/TF
    # =========================================================

    navigation_lifecycle_manager = TimerAction(
        period=10.0,
        actions=[
            Node(
                package="nav2_lifecycle_manager",
                executable="lifecycle_manager",
                name="lifecycle_manager_navigation",
                output="screen",
                parameters=[
                    {
                        "use_sim_time": True,
                        "autostart": True,
                        "node_names": [
                            "planner_server",
                            "controller_server",
                            "behavior_server",
                            "bt_navigator"
                        ]
                    }
                ]
            )
        ]
    )

    # =========================================================
    # LAUNCH
    # =========================================================

    return LaunchDescription([
        ekf,

        map_server,
        amcl_server,
        localization_lifecycle_manager,

        planner,
        controller,
        behavior_server,
        bt_navigator,

        navigation_lifecycle_manager
    ])