L = []
while True:
    try:
        n = int(input("Nhập số lượng phần tử: "))
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

co_chan = False
co_le = False

for x in L:
    if x % 2 == 0:
        co_chan = True
    else:
        co_le = True

if co_chan and co_le:
    print("True – Đây là list chẵn lẻ")
else:
    print("False – Đây không phải list chẵn lẻ")
