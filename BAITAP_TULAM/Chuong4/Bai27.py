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
    item = input(f"Nhập phần tử thứ {i+1}: ")
    try:
        value = int(item)
        L.append(value)
    except ValueError:
        if item.strip() == "":
            print("Không được nhập chuỗi rỗng, tự động gán thành ''")
            L.append("")
        else:
            L.append(item)
print("\nList L đã nhập:", L)
ds_chuoi = []
ds_so = []
for x in L:
    if isinstance(x, str):
        ds_chuoi.append(x)
    elif isinstance(x, int):
        ds_so.append(x)

if len(ds_chuoi) > 0:
    chuoi_dai_nhat = ds_chuoi[0]
    for c in ds_chuoi:
        if len(c) > len(chuoi_dai_nhat):
            chuoi_dai_nhat = c
else:
    chuoi_dai_nhat = None

if len(ds_so) > 0:
    so_nho_nhat = ds_so[0]
    for s in ds_so:
        if s < so_nho_nhat:
            so_nho_nhat = s
else:
    so_nho_nhat = None
print("Chuỗi dài nhất:", chuoi_dai_nhat)
print("Số nguyên nhỏ nhất:", so_nho_nhat)
