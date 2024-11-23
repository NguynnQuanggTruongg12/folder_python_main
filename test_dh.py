import numpy as np
from scipy.optimize import fsolve

# Hàm tính toán động học nghịch đảo
def inverse_kinematics(Px, Py, Pz, l1, l2, l3):
    # Tính 2 giá trị của q1
    q1_solution1 = np.arctan2(Py, Px)
    q1_solution2 = np.arctan2(-Py, -Px)

    # Hàm để giải hệ phương trình cho q2 và q3
    def equations(vars):
        q2, q3 = vars
        eq1 = l1 + l3 * np.sin(q2 + q3) + l2 * np.cos(q2) - Pz   # Phương trình cho Pz
        eq2 = l3 * np.cos(q2 + q3) + l2 * np.sin(q2) - np.sqrt(Px**2 + Py**2)  # Tính r = sqrt(Px^2 + Py^2)
        return [eq1, eq2]

    # Sử dụng fsolve để giải hệ phương trình
    initial_guess = [0, 0]  # Giá trị ban đầu cho q2 và q3
    q2_solution1, q3_solution1 = fsolve(equations, initial_guess)

    # Chuyển đổi kết quả từ radian sang độ
    q1_solution1_deg = np.degrees(q1_solution1)
    q2_solution1_deg = np.degrees(q2_solution1)
    q3_solution1_deg = np.degrees(q3_solution1)

    # Tính giá trị tổng của q2 và q3 nếu cần thiết
    q3_sum_deg = q2_solution1_deg + q3_solution1_deg

    # Trả về kết quả
    return q1_solution1_deg, q2_solution1_deg, q3_solution1_deg, q3_sum_deg

# Ví dụ sử dụng hàm inverse_kinematics
l1 = 180
l2 = 150
l3 = 170
Px = 200
Py = 120
Pz = 40

q1, q2, q3, q3_sum = inverse_kinematics(Px, Py, Pz, l1, l2, l3)

# Hiển thị kết quả
print('Giá trị của q1 (độ) là:', q1)
print('Giá trị của q2 (độ) là:', q2)
print('Giá trị của q3 (độ) là:', q3)
print('Tổng q2 và q3 (độ) là:', q3_sum)
