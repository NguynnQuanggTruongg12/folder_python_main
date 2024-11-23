import sys
import rospy
from PyQt5.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsPixmapItem, QGraphicsEllipseItem
from PyQt5.QtGui import QImage, QPixmap, QBrush, QColor
from PyQt5.QtCore import QTimer, Qt
from nav_msgs.msg import OccupancyGrid, Odometry
import numpy as np

class MapWidget(QGraphicsView):
    def __init__(self):
        super(MapWidget, self).__init__()
        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)

        # Item hiển thị bản đồ
        self.map_item = QGraphicsPixmapItem()
        self.scene.addItem(self.map_item)

        # Item hiển thị vị trí robot (hình tròn đỏ)
        self.robot_item = QGraphicsEllipseItem(-5, -5, 10, 10)  # Kích thước hình tròn (10x10 pixel)
        self.robot_item.setBrush(QBrush(QColor("red")))
        self.scene.addItem(self.robot_item)

    def update_map(self, map_image):
        pixmap = QPixmap.fromImage(map_image)
        self.map_item.setPixmap(pixmap)

    def update_robot_position(self, x, y):
        # Đặt vị trí của hình tròn robot theo tọa độ trên bản đồ
        self.robot_item.setPos(x, y)

def occupancy_grid_to_qimage(occupancy_grid):
    width = occupancy_grid.info.width
    height = occupancy_grid.info.height
    data = np.array(occupancy_grid.data).reshape((height, width))
    
    # Chuyển đổi giá trị từ -1, 0-100 thành màu (0 là trắng, 100 là đen)
    image = np.zeros((height, width, 3), dtype=np.uint8)
    image[data == -1] = [128, 128, 128]  # Xám cho các ô không xác định
    image[data == 0] = [255, 255, 255]   # Trắng cho các ô trống
    image[data > 0] = [0, 0, 0]          # Đen cho các ô có chướng ngại vật

    qimage = QImage(image.data, width, height, QImage.Format_RGB888)
    return qimage.mirrored()  # Để bản đồ hiển thị đúng chiều

def map_callback(msg):
    global map_widget
    qimage = occupancy_grid_to_qimage(msg)
    map_widget.update_map(qimage)

def odom_callback(msg):
    global map_widget
    # Lấy tọa độ x, y từ thông tin vị trí trong Odometry
    x = msg.pose.pose.position.x
    y = msg.pose.pose.position.y

    # Tính toán tọa độ trên QGraphicsScene (có thể cần phải scale theo bản đồ)
    map_resolution = 0.05  # Giả sử độ phân giải là 0.05m/pixel, điều chỉnh theo thực tế
    map_origin_x = 0       # Gốc tọa độ của bản đồ, điều chỉnh theo thực tế
    map_origin_y = 0

    # Chuyển đổi tọa độ x, y từ thế giới thực sang tọa độ pixel trên bản đồ
    scene_x = (x - map_origin_x) / map_resolution
    scene_y = -(y - map_origin_y) / map_resolution  # Đảo chiều y để khớp với hệ tọa độ Qt

    map_widget.update_robot_position(scene_x, scene_y)

def ros_spin():
    rospy.rostime.wallsleep(0.01)  # Đảm bảo không chặn luồng chính của Qt

if __name__ == "__main__":
    rospy.init_node('qt_map_display')

    app = QApplication(sys.argv)
    map_widget = MapWidget()
    map_widget.setWindowTitle("Real-Time Map and Robot Position Display")
    map_widget.show()

    rospy.Subscriber("map", OccupancyGrid, map_callback)
    rospy.Subscriber("odom", Odometry, odom_callback)

    timer = QTimer()
    timer.timeout.connect(ros_spin)
    timer.start(10)  # Cập nhật mỗi 10ms để ROS xử lý

    sys.exit(app.exec_())
