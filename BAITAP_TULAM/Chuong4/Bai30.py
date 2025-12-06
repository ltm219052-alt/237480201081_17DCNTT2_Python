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
        s = input(f"Nhập chuỗi thứ {i+1}: ")
        if s.strip() == "":
            print("Chuỗi không được rỗng, hãy nhập lại!")
            continue
        hop_le = True
        for c in s:
            if not (c.isalpha() or c == " "):
                hop_le = False
                break
        if hop_le:
            L.append(s)
            break
        else:
            print("Chuỗi chỉ được chứa chữ cái và khoảng trắng!")
print("\nList L đã nhập:", L)
def vi_tri_in_hoa_lon_nhat(s):
    vt = -1
    for i in range(len(s)):
        if s[i].isupper():
            vt = i
    return vt
chi_so_max = 0
gia_tri_max = vi_tri_in_hoa_lon_nhat(L[0])
for i in range(1, len(L)):
    vt = vi_tri_in_hoa_lon_nhat(L[i])
    if vt > gia_tri_max:
        gia_tri_max = vt
        chi_so_max = i
print("Chuỗi có vị trí ký tự in HOA lớn nhất nằm ở vị trí (khi nhập):", chi_so_max + 1)
print("Nội dung chuỗi đó là:", L[chi_so_max])
print("Vị trí ký tự in HOA lớn nhất trong chuỗi:", gia_tri_max)
