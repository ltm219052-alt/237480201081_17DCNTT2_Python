L = []
while True:
    try:
        n = int(input("hập số lượng phần tử: "))
        break
    except ValueError:
        print("Nhập số bất kỳ!")

for i in range(n):
    while True:
        try:
            x = int(input(f"Nhập phần tử thứ {i + 1}: "))
            L.append(x)
            break
        except ValueError:
            print("Nhập số nguyên hợp lệ!")

chan = []
khong = []
le = []

for x in L:
    if x == 0:
        khong.append(x)
    elif x % 2 == 0:
        chan.append(x)
    else:
        le.append(x)

ket_qua = chan + khong + le
print("List sau khi sắp xếp:", ket_qua)
