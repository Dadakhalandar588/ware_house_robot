from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'my_robot_controller'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name,
            ['package.xml']),
        (os.path.join('share', package_name, 'launch'),
            glob('launch/*.launch.py')),
        (os.path.join('share',package_name,'urdf'),
         glob('urdf/*')),
        (os.path.join('share',package_name,'gazebo_workspaces'),
         glob('gazebo_workspaces/*'))

    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='khalandar-workspace',
    maintainer_email='khalandar-workspace@todo.todo',
    description='Robot controller package',
    license='Apache License 2.0',
    extras_require={
        'test': ['pytest'],
    },
    entry_points={
        'console_scripts': [
            'test_node = my_robot_controller.my_first_node:main',
            'draw_circle = my_robot_controller.draw_circle:main',
            'draw_rectangle = my_robot_controller.draw_rectangle:main',
            'create_subscriber = my_robot_controller.sub:main',
            'control = my_robot_controller.control:main',
            'turtle_broadcasting = my_robot_controller.turtle_broadcasting:main',
            'turtle2_control=my_robot_controller.turtle2_control:main',
            'turtle2_broadcaster=my_robot_controller.turtle2_broadcaster:main',
            'turtle3_broadcaster=my_robot_controller.turtle3:main',
            'turtle4_broadcaster=my_robot_controller.turtle4:main',
            'turtle5_broadcaster=my_robot_controller.turtle5:main',
            'turtle1_broadcaster=my_robot_controller.turtle1:main'  
        ],
    },
)