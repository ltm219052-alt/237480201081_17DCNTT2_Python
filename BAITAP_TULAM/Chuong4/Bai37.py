def nhap_list_so_nguyen():
    while True:
        try:
            n = int(input("Nhập số lượng phần tử của list: "))
            if n <= 0:
                print("Số lượng phải > 0!")
                continue
            break
        except ValueError:
            print("Vui lòng nhập số nguyên!")
    L = []
    for i in range(n):
        while True:
            try:
                x = int(input(f"Nhập phần tử thứ {i+1}: "))
                L.append(x)
                break
            except ValueError:
                print("Vui lòng nhập số nguyên!")
    return L
# Hàm sắp xếp tăng dần và giảm dần
def sap_xep(L):
    tang_dan = sorted(L)
    giam_dan = sorted(L, reverse=True)
    return tang_dan, giam_dan
L = nhap_list_so_nguyen()
print("List đã nhập:", L)
tang, giam = sap_xep(L)
print("Sắp xếp tăng dần:", tang)
print("Sắp xếp giảm dần:", giam)
