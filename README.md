<p align="center">
  <img
    height="300"
    alt="Robin Logo"
    src="client/public/icon.svg"/>
</p>

# Robin

Robin is a debug controller UI for robots developed by [PyLoT Robotics](https://pylot.kaijo-physics.club).

## Installation

### Prerequisites

- ROS 2 environment (tested as an `ament_python` package)
- `bun` (used to run the web client)
- `rosbridge_server` (for WebSocket connection from browser)
- Python dependencies used by this package (`rclpy`, `cv_bridge`, `opencv-python`, etc.)

### Build this package

From your ROS 2 workspace root:

```bash
colcon build --packages-select robin
source install/setup.bash
```

### Install client dependencies

```bash
cd perception/PyLoT-Face/client
bun install
```

## Usage

### Startup

Run the following commands in order:

```bash
ros2 launch rosbridge_server rosbridge_websocket_launch.xml # Start RosBridge Server
ros2 run robin video_publisher # Start node for video streaming
ros2 run robin client # Start app (open from the displayed QR code)
```

The `video_publisher` node subscribes to `face` (`sensor_msgs/msg/Image`) and publishes `/face_image_base64` (`std_msgs/msg/String`) for the web UI.

### Text input method

Robin supports text input for connection settings:

1. Open the settings modal (`⚙️`).
2. Enter the WebSocket URL in the text field (example: `ws://localhost:9090`).
3. Press `CLOSE` to save and reload.

### Image input method

Robin receives image input from the ROS topic `face`.

Option A: Publish from a live camera node to `face`.

Option B: Publish a test image file from command line:

```bash
ros2 run image_publisher image_publisher_node /path/to/image.jpg --ros-args -r image_raw:=/face
```

If `image_publisher` is not installed, install the package providing it in your ROS 2 distribution and run the command again.