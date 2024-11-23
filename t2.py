import os
import signal
import subprocess
import time

def restart_roslaunch():
    try:
        # Tìm và tắt các process đang chạy lệnh
        pids = subprocess.check_output(["pgrep", "-f", "roslaunch navigation_bot move_base_qd.launch"], text=True).strip().split()
        for pid in pids:
            os.kill(int(pid), signal.SIGTERM)
        print("Đã tắt terminal chạy move_base_qd.launch.")
    except subprocess.CalledProcessError:
        print("Không tìm thấy terminal đang chạy move_base_qd.launch.")
    except Exception as e:
        print(f"Lỗi: {e}")
    
    time.sleep(2)  # Đợi trước khi khởi động lại
    print("Khởi động lại move_base_qd.launch...")
    os.system('gnome-terminal -- roslaunch navigation_bot move_base_qd.launch')

restart_roslaunch()
