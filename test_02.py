# import serial
# import time

# # Set up the serial connection (adjust 'COM3' or '/dev/ttyUSB0' and baud rate as needed)

# # time.sleep(2)  # Wait for connection to establish

# def send_data_over_uart(data1, data2, data3, data4):
#     ser = serial.Serial('/dev/ttyUSB2', 9600)  # Replace with your Arduino port and baud rate
#     # Format the data with semicolon separators
#     message = f"{data1};{data2};{data3};{data4};"
#     ser.write(message.encode())  # Send the encoded message over UART
#     print("Sent:", message)
#     ser.close()

# # Example usage
# send_data_over_uart('A', 'B', 'C', 'D')  # Replace with your desired characters

# # Close the serial port when done

import serial
import time

# Cấu hình cổng serial
arduino_port = "/dev/ttyUSB1"  # Thay bằng cổng COM của bạn (Windows) hoặc "/dev/ttyUSB0" trên Linux
baudrate = 115200

# Kết nối tới Arduino
ser = serial.Serial(arduino_port, baudrate, timeout=1)
time.sleep(2)  # Chờ Arduino khởi động

def send_data(xd1, xd2, xd3, gripper):
    """
    Gửi dữ liệu tới Arduino qua serial.
    :param xd1: Giá trị float đầu tiên
    :param xd2: Giá trị float thứ hai
    :param xd3: Giá trị float thứ ba
    :param gripper: Giá trị integer thứ tư
    """
    # Định dạng dữ liệu theo định dạng Arduino mong đợi
    data = f"{xd1};{xd2};{xd3};{gripper}\n"
    ser.write(data.encode('utf-8'))
    print(f"Dữ liệu đã gửi: {data.strip()}")

try:
    while True:
        # Thay đổi các giá trị để thử nghiệm
        xd1 =  -10
        xd2 = -10
        xd3 = -10
        gripper = 0

        # Gửi dữ liệu tới Arduino
        send_data(xd1, xd2, xd3, gripper)

        # Chờ 1 giây trước lần gửi tiếp theo
        time.sleep(1)

except KeyboardInterrupt:
    print("Kết thúc chương trình.")
finally:
    # Đóng cổng serial
    ser.close()
