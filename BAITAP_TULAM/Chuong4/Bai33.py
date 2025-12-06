def nhap_list_chuoi():
    while True:
        try:
            n = int(input("Nhập số lượng phần tử của list L: "))
            if n <= 0:
                print("Số lượng phải > 0!")
                continue
            break
        except ValueError:
            print("Vui lòng nhập số nguyên!")
    L = []
    for i in range(n):
        while True:
            s = input(f"Nhập chuỗi thứ {i+1}: ").strip()
            if s == "":
                print("Chuỗi không được rỗng!")
            else:
                L.append(s)
                break
    return L
def ma_hoa_list(L):
    D = {}          # dictionary mã hóa
    ma = 0          # mã bắt đầu từ 0
    # Tạo dictionary mã hóa
    for item in L:
        if item not in D:
            D[item] = ma
            ma += 1
    # Tạo list đã mã hóa
    encoded_list = []
    for item in L:
        encoded_list.append(D[item])
    return D, encoded_list
L = nhap_list_chuoi()
print("List đã nhập:", L)
D, K = ma_hoa_list(L)
print("\nDictionary mã hóa:", D)
print("List sau khi mã hóa:", K)
