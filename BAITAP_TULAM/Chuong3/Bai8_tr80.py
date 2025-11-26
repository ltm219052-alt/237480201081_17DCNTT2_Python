def la_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def so_nguyen_to_trong_list(L, a):
    result = []
    for x in L:
        if la_nguyen_to(x):
            result.append(x)
            if len(result) == a:
                break
    return result
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
kq = so_nguyen_to_trong_list(lst, k)
print("Kết quả:", kq)
