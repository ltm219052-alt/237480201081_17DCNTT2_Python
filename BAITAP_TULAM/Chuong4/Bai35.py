def nhap_list_so():
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
# In số chẵn trong list
def in_so_chan(L):
    print("Các số chẵn trong list:")
    for num in L:
        if num % 2 == 0:
            print(num)
        else:
            pass   # không cần làm gì với số lẻ
L = nhap_list_so()
print("List đã nhập:", L)
in_so_chan(L)
