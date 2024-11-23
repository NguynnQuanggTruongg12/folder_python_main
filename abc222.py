import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry

class RobotController:
    def __init__(self):
        # Khởi tạo node ROS
        rospy.init_node('robot_move_to_goal', anonymous=True)

        # Publisher cho /cmd_vel để gửi lệnh di chuyển
        self.pub_twist = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

        # Biến toàn cục
        self.datientoi = True  # Biến kiểm tra di chuyển đến vị trí mục tiêu
        self.error_x = 0      # Sai số hiện tại về vị trí X

        # Vị trí mục tiêu
        self.x_goal = 0  # Chỉnh giá trị mục tiêu tại đây

        # Lắng nghe dữ liệu từ /odom
        rospy.Subscriber('/slamware_ros_sdk_server_node/odom', Odometry, self.odom_callback)

    def odom_callback(self, data):
        """
        Callback xử lý dữ liệu từ /odom, tính toán sai số theo trục X.
        """
        # Lấy dữ liệu vị trí x từ /odom
        x_odem = data.pose.pose.position.x

        # Tính sai số theo trục X
        self.error_x = x_odem - self.x_goal

        # Tạo đối tượng Twist để điều khiển robot
        twist_msg = Twist()

        # Điều khiển robot di chuyển tới vị trí mục tiêu
        if self.datientoi:
            if abs(self.error_x) > 0.05:  # Nếu sai số lớn hơn ngưỡng
                twist_msg.linear.x = -0.2 if self.error_x > 0 else 0.2
                self.pub_twist.publish(twist_msg)
                rospy.loginfo(f"Đang di chuyển: Lỗi X hiện tại {self.error_x:.2f}m")
            else:
                twist_msg.linear.x = 0
                self.pub_twist.publish(twist_msg)
                rospy.loginfo(f"Đã đạt vị trí mục tiêu: Lỗi X hiện tại {self.error_x:.2f}m")
                self.datientoi = False  # Đã di chuyển đến vị trí mục tiêu

    def move_to_goal(self):
        """
        Hàm này bắt đầu quá trình di chuyển robot đến mục tiêu.
        """
        while self.datientoi:
            rospy.sleep(0.1)  # Chờ một chút trước khi kiểm tra lại
            rospy.loginfo("Đang tiếp tục kiểm tra trạng thái di chuyển...")

        rospy.loginfo("Hoàn thành nhiệm vụ.")

if __name__ == '__main__':
    try:
        # Tạo đối tượng điều khiển robot và bắt đầu di chuyển
        controller = RobotController()
        controller.move_to_goal()

    except rospy.ROSInterruptException:
        pass
