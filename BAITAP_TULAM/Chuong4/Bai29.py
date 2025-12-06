while True:
    try:
        n = int(input("Nhập số lượng phần tử của list L: "))
        if n <= 0:
            print("Số lượng phần tử phải lớn hơn 0!")
        else:
            break
    except ValueError:
        print("Vui lòng nhập số nguyên bất kỳ!")
L = []
for i in range(n):
    while True:
        chuoi = input(f"Nhập chuỗi thứ {i+1}: ")
        if chuoi.strip() == "": # Kiểm tra rỗng
            print("Chuỗi không được rỗng, hãy nhập lại!")
            continue
        hop_le = True # Kiểm tra ký tự hợp lệ (chỉ chữ và khoảng trắng)
        for c in chuoi:
            if not (c.isalpha() or c == " "):
                hop_le = False
                break
        if hop_le:
            L.append(chuoi)
            break
        else:
            print("Chuỗi chỉ được chứa chữ cái và khoảng trắng! Hãy nhập lại.")
print("\nList L đã nhập:", L)
def dem_so_tu(s): # Hàm đếm số từ: tách theo khoảng trắng
    danh_sach = s.split()
    return len(danh_sach)
vi_tri_max = 0
so_tu_max = dem_so_tu(L[0])
for i in range(1, len(L)): # Tìm chuỗi có nhiều từ nhất
    so_tu = dem_so_tu(L[i])
    if so_tu > so_tu_max:
        so_tu_max = so_tu
        vi_tri_max = i
print("Chuỗi có nhiều từ nhất nằm ở vị trí:", vi_tri_max)
print("Nội dung chuỗi đó là:", L[vi_tri_max])
print("Số lượng từ trong chuỗi:", so_tu_max)
