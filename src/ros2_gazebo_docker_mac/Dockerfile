FROM ros:jazzy-ros-core

RUN apt-get update \
    && apt-get install -y \
    wget curl unzip \
    lsb-release \
    mesa-utils \
    build-essential \
    && apt-get clean

RUN apt-get update && apt-get install -y \
    ros-jazzy-desktop-full

RUN apt-get update \
    && apt-get install -y \
    python3-colcon-common-extensions python3-rosdep --no-install-recommends \
    && apt-get clean
RUN rosdep init && rosdep update

# install python3 and numpy
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y
