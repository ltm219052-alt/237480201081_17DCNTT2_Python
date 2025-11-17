sinh_vien = []
def them_sinh_vien():
    ma = input("Nhập mã sinh viên: ")
    for sv in sinh_vien:
        if sv['ma'] == ma:
            print("Mã sinh viên đã tồn tại!")
            return
    ten = input("Nhập tên sinh viên: ")
    sinh_vien.append({'ma': ma, 'ten': ten})
    print("Đã thêm sinh viên thành công!")


def xoa_sinh_vien():
    ma = input("Nhập mã sinh viên cần xóa: ")
    for sv in sinh_vien:
        if sv['ma'] == ma:
            sinh_vien.remove(sv)
            print("Đã xóa sinh viên!")
            return
    print("Không tìm thấy sinh viên với mã này!")


def sua_sinh_vien():
    ma = input("Nhập mã sinh viên cần sửa: ")
    for sv in sinh_vien:
        if sv['ma'] == ma:
            ten_moi = input(f"Nhập tên mới cho sinh viên {ma}: ")
            sv['ten'] = ten_moi
            print("Đã cập nhật thông tin sinh viên!")
            return
    print("Không tìm thấy sinh viên với mã này!")


def xem_danh_sach():
    if not sinh_vien:
        print("Danh sách sinh viên rỗng!")
    else:
        print("Danh sách sinh viên:")
        for sv in sinh_vien:
            print(f"Mã: {sv['ma']}, Tên: {sv['ten']}")


# Menu chính
while True:
    print("\n--- QUẢN LÝ SINH VIÊN ---")
    print("1. Thêm sinh viên")
    print("2. Xóa sinh viên")
    print("3. Sửa sinh viên")
    print("4. Xem danh sách sinh viên")
    print("0. Thoát")

    chon = input("Chọn chức năng: ")

    if chon == "1":
        them_sinh_vien()
    elif chon == "2":
        xoa_sinh_vien()
    elif chon == "3":
        sua_sinh_vien()
    elif chon == "4":
        xem_danh_sach()
    elif chon == "0":
        print("Thoát chương trình!")
        break
    else:
        print("Lựa chọn không hợp lệ, vui lòng chọn lại.")
