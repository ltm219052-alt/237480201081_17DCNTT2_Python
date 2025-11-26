def trung_binh_a_phan_tu(L, a):
    if a > len(L):
        return None
    return sum(L[:a]) / a

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
        k = int(input("Nhập số nguyên k: "))
        break
    except ValueError:
        print("nhập phần tử tìm vi!")
kq = trung_binh_a_phan_tu(lst, k)
if kq is None:
    print("Không thể tính trung bình vì số phần tử nhỏ hơn a.")
else:
    print(f"Giá trị trung bình của {k} phần tử đầu tiên là: {kq}")
