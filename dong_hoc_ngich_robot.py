import math

def forward_kinematics_3DOF(theta1, theta2, theta3):
    # Link lengths
    l1 = 18
    l2 = 15
    l3 = 17

    # Calculate the end-effector position
    Px = math.cos(math.radians(theta1)) * (l3 * math.cos(math.radians(theta2 + theta3)) + l2 * math.cos(math.radians(theta2)))
    Py = math.sin(math.radians(theta1)) * (l3 * math.cos(math.radians(theta2 + theta3)) + l2 * math.cos(math.radians(theta2)))
    Pz = l3 * math.sin(math.radians(theta2 + theta3)) + l2 * math.sin(math.radians(theta2))

    return Px, Py, Pz

# Example usage with given angles theta1, theta2, theta3
theta1 = 30  # Replace with actual value
theta2 = 45  # Replace with actual value
theta3 = 60  # Replace with actual value

Px, Py, Pz = forward_kinematics_3DOF(theta1, theta2, theta3)
print("Px:", Px)
print("Py:", Py)
print("Pz:", Pz)
