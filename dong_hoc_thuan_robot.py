import math
import numpy as np

def calculate_angles(Px, Py, Pz):
    # Robot link lengths
    L2 = 15
    L3 = 17

    # Calculate theta1
    s1_1 = Py
    c1_1 = Px
    t1_1 = math.degrees(math.atan2(s1_1, c1_1))

    # Calculate theta3
    c3_1 = ((Px * math.cos(math.radians(t1_1)) + Py * math.sin(math.radians(t1_1)))**2 + Pz**2 - L3**2 - L2**2) / (2 * L2 * L3)
    s3_1 = math.sqrt(1 - c3_1**2)
    t3_1 = math.degrees(math.atan2(s3_1, c3_1))

    # Calculate theta2 using determinant method
    d_1 = np.array([[L3 * math.cos(math.radians(t3_1)) + L2, -L3 * math.sin(math.radians(t3_1))],
                    [L3 * math.sin(math.radians(t3_1)), L3 * math.cos(math.radians(t3_1)) + L2]])
    
    dc_1 = np.array([[Px * math.cos(math.radians(t1_1)) + Py * math.sin(math.radians(t1_1)), -L3 * math.sin(math.radians(t3_1))],
                     [Pz, L3 * math.cos(math.radians(t3_1)) + L2]])
    
    ds_1 = np.array([[L3 * math.cos(math.radians(t3_1)) + L2, Px * math.cos(math.radians(t1_1)) + Py * math.sin(math.radians(t1_1))],
                     [L3 * math.sin(math.radians(t3_1)), Pz]])
    
    c2_1 = np.linalg.det(dc_1) / np.linalg.det(d_1)
    s2_1 = np.linalg.det(ds_1) / np.linalg.det(d_1)
    t2_1 = math.degrees(math.atan2(s2_1, c2_1))

    # Return the angles
    return t1_1, t2_1, t3_1

# Example usage with given Px, Py, Pz
Px = 10  # Replace with actual value
Py = 20  # Replace with actual value
Pz = 30  # Replace with actual value

t1_1, t2_1, t3_1 = calculate_angles(Px, Py, Pz)
print("Theta1:", t1_1)
print("Theta2:", t2_1)
print("Theta3:", t3_1)
