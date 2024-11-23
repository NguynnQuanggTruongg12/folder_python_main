import os
import subprocess
import time

def main():
    os.system('gnome-terminal -- roscore')
    time.sleep(2)
    # Mở terminal và chạy lệnh để khởi động move_base_qd.launch
    os.system('gnome-terminal -- roslaunch navigation_bot move_base_qd.launch')

    # Mở terminal và chạy lệnh để khởi động slamware_ros_sdk_server_node
    os.system('gnome-terminal -- roslaunch slamware_ros_sdk slamware_ros_sdk_server_node.launch ip_address:=192.168.11.1')

    # Mở terminal và chạy lệnh để khởi động rosserial_python serial_node
    os.system('gnome-terminal -- rosrun rosserial_python serial_node.py /dev/ttyUSB0')



if __name__ == '__main__':
    main()
