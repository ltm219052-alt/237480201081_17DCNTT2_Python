def gia_tri_lon_thu_a(L, a):
    if a <= 0 or a > len(L):
        return None
    sorted_L = sorted(L, reverse=True)
    return sorted_L[a-1]
while True:
    try:
        n = int(input("Nhập n: "))
        break
    except ValueError:
        print("nhập số bất kỳ!")
lst=[]
for i in range(n):
    while True:
        try:
            x=int(input(f"Nhập phần tử thứ {i+1}: "))
            lst.append(x)
            break
        except ValueError:
            print("Vui lòng nhập số nguyên hợp lệ!")
while True:
    try:
        k = int(input("Nhập thứ hạng cần tìm: "))
        break
    except ValueError:
        print("nhập phần tử tìm vi!")
kq = gia_tri_lon_thu_a(lst, k)
if kq is None:
    print("Không có giá trị lớn thứ", k)
else:
    print(f"Giá trị lớn thứ {k} là: {kq}")