#include <memory>
#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"
#include "sjtu_drone_autopilot/field.hpp"

using std::placeholders::_1;

class AutopilotNode : public rclcpp::Node
{
public:
  AutopilotNode()
  : Node("autopilot_node")
  {
    subscription_ = this->create_subscription<std_msgs::msg::String>(
      "chatter", 10, std::bind(&AutopilotNode::topic_callback, this, _1));

    field_ = std::make_shared<Field>(); 
    field_->generate();
    field_->query();
  }

private:
  void topic_callback(const std_msgs::msg::String::SharedPtr msg) const
  {
    RCLCPP_INFO(this->get_logger(), "Listening to: '%s'", msg->data.c_str());
  }
  
  rclcpp::Subscription<std_msgs::msg::String>::SharedPtr subscription_;

  std::shared_ptr<Field> field_;
};

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<AutopilotNode>());
  rclcpp::shutdown();
  return 0;
}