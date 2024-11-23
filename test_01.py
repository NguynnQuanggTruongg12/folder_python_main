import mysql.connector

# Kết nối tới cơ sở dữ liệu MySQL
def connect_db():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="robot",  # Thay thế bằng tên người dùng của bạn
        password="123456",  # Thay thế bằng mật khẩu của bạn
        database="sys"  # Thay thế bằng tên cơ sở dữ liệu của bạn
    )

# Hàm để lưu giá trị vào MySQL
def save_values(x, y, z, w, id):
    try:
        db = connect_db()
        cursor = db.cursor()
        cursor.execute("INSERT INTO `robot` (x, y, z, w, id) VALUES (%s, %s, %s, %s, %s)", (x, y, z, w, id))
        db.commit()
        print("Values saved successfully!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        db.close()
def get_values_by_id(id):
    try:
        db = connect_db()
        cursor = db.cursor()
        cursor.execute("SELECT x, y, z, w FROM `robot` WHERE id = %s", (id,))
        result = cursor.fetchone()  # Lấy một dòng dữ liệu

        if result:
            print(f"Values for ID {id}: x = {result[0]}, y = {result[1]}, z = {result[2]}, w = {result[3]}")
        else:
            print(f"No values found for ID {id}.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        db.close()

save_values(0,0,0,1,200)
# get_values_by_id(6)