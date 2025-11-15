while True:
    try:
        n = int(input("Nhập n: "))

    except ValueError:
        print("nhập số bất kỳ!")

    L = []
    for i in range(n):
        x = int(input(f"Nhập phần tử thứ {i+1}: "))
        L.append(x)

    duong_dau_tien = -1
    for x in L:
        if x > 0:
            duong_dau_tien = x
            break

    print("Giá trị dương đầu tiên là:", duong_dau_tien)
    break