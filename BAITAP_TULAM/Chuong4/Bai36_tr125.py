def nhap_danh_sach():
    while True:
        try:
            n = int(input("Nhập số lượng sinh viên: "))
            if n <= 0:
                print("Số lượng phải > 0!")
                continue
            break
        except ValueError:
            print("Vui lòng nhập số nguyên!")
    ds = []
    for i in range(n):
        while True:
            ten = input(f"Nhập tên sinh viên thứ {i+1}: ").strip()
            if ten == "":
                print("Tên không được để trống!")
            else:
                ds.append(ten)
                break
    return ds
def tim_kiem(ds):
    ten_can_tim = input("Nhập tên cần tìm: ").strip()
    tim_thay = False
    for i in range(len(ds)):
        if ds[i].lower() == ten_can_tim.lower():  # so sánh không phân biệt hoa thường
            print(f">>> Tìm thấy '{ten_can_tim}' ở vị trí {i} trong danh sách.")
            tim_thay = True
            break
    if not tim_thay:
        print(f">>> Không tìm thấy '{ten_can_tim}' trong danh sách.")
danh_sach = nhap_danh_sach()
print("Danh sách sinh viên đã nhập:", danh_sach)

tim_kiem(danh_sach)
