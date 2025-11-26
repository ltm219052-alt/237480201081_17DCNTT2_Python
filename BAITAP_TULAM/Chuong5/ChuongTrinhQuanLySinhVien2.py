# main.py
import ChuongTrinhQuanLySinhVien1 as sm

def menu():
    """Hiển thị menu chọn chức năng"""
    print("\nChương trình quản lý sinh viên")
    print("1. Thêm sinh viên")
    print("2. Xóa sinh viên")
    print("3. Sửa thông tin sinh viên")
    print("4. Xem danh sách sinh viên")
    print("5. Thoát")

def main():
    """Chương trình chính để quản lý sinh viên"""
    while True:
        menu()
        choice = input("Chọn chức năng (1-5): ")

        if choice == "1":
            student_id = input("Nhập mã sinh viên: ")
            student_name = input("Nhập tên sinh viên: ")
            sm.add_student(student_id, student_name)

        elif choice == "2":
            student_id = input("Nhập mã sinh viên cần xóa: ")
            sm.remove_student(student_id)

        elif choice == "3":
            student_id = input("Nhập mã sinh viên cần sửa: ")
            new_name = input("Nhập tên mới của sinh viên: ")
            sm.update_student(student_id, new_name)

        elif choice == "4":
            sm.view_students()

        elif choice == "5":
            print("Cảm ơn bạn đã sử dụng chương trình.")
            break

        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

if __name__ == "__main__":
    main()
