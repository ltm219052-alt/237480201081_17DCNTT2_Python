while True:
    try:
        n = int(input("Nhập n: "))
        break
    except ValueError:
        print("Nhập số bất kỳ!")

L = []
for i in range(n):
    while True:
        try:
            x = int(input(f"Nhập phần tử thứ {i+1}: "))
            L.append(x)
            break
        except ValueError:
            print("Nhập số nguyên hợp lệ!")

while True:
    try:
        x = int(input("Nhập giá trị x: "))
        break
    except ValueError:
        print("Nhập số bất kỳ!")

max_kc = -1
gia_tri_xa_nhat = None

for value in L:
    khoang_cach = abs(value - x)
    if khoang_cach > max_kc:
        max_kc = khoang_cach
        gia_tri_xa_nhat = value

print("Giá trị xa x nhất trong list là:", gia_tri_xa_nhat)
