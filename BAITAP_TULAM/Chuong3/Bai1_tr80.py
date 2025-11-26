def bang_cuu_chuong_lon_hon(a, b):
    n = max(a, b)
    print(f"Bảng cửu chương của {n}:")
    for i in range(1, 10):
        print(f"{n} x {i} = {n*i}")

a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))
bang_cuu_chuong_lon_hon(a, b)
