# student_management.py
students = []

def add_student(student_id, student_name):
    """Thêm sinh viên vào danh sách"""
    students.append({"id": student_id, "name": student_name})
    print(f"Đã thêm sinh viên: {student_name} (Mã sinh viên: {student_id})")

def remove_student(student_id):
    """Xóa sinh viên khỏi danh sách theo mã sinh viên"""
    global students
    students = [student for student in students if student["id"] != student_id]
    print(f"Đã xóa sinh viên với mã: {student_id}")

def update_student(student_id, new_name):
    """Sửa thông tin sinh viên"""
    for student in students:
        if student["id"] == student_id:
            student["name"] = new_name
            print(f"Đã sửa tên sinh viên với mã {student_id} thành {new_name}")
            return
    print(f"Không tìm thấy sinh viên với mã: {student_id}")

def view_students():
    """Xem danh sách sinh viên"""
    if not students:
        print("Danh sách sinh viên hiện tại trống.")
        return
    print("Danh sách sinh viên:")
    for student in students:
        print(f"Mã sinh viên: {student['id']}, Tên sinh viên: {student['name']}")
