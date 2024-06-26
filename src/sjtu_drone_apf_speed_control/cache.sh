mkdir ./cache
curl -L https://github.com/osrf/gazebo_models/archive/refs/heads/master.zip -o ./cache/gazebo_models.zip
unzip ./cache/gazebo_models.zip -d ./cache


# on docker
# mkdir -p ~/.gazebo/models/
# mv ./tmp/gazebo_models-master/* ~/.gazebo/models/