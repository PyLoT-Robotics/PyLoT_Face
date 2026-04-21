from setuptools import find_packages, setup

package_name = 'pylot_face'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='pylot',
    maintainer_email='johndoe@example.com',
    description='Mobile Robot Controller for PyLoT Robotics',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'client = pylot_face.client:main',
            'video_publisher = pylot_face.video_publisher:main'
        ],
    },
)
