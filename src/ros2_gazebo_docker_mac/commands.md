docker run --rm \
    --env="DISPLAY=$IP:0" \
    --volume="$HOME/.Xauthority:/root/.Xauthority:rw" \
    --net ros-network \
    ros2_jazzy ros2 run rviz2 rviz2

    