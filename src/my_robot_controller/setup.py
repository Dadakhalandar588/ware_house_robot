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
         glob('gazebo_workspaces/*')),
        (os.path.join('share',package_name,'warehouse_map'),
         glob('warehouse_map/*')),
        (os.path.join('share', package_name, 'config'),
         glob('config/*.yaml')),

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
        ],
    },
)