while True:
    try:
        n = int(input("Nhập số lượng phần tử của list L: "))
        if n <= 0:
            print("Số lượng phần tử phải lớn hơn 0!")
        else:
            break
    except ValueError:
        print("Vui lòng nhập số bất kỳ!")
L = []
for i in range(n):
    item = input(f"Nhập phần tử thứ {i+1}: ")

    try:
        value = int(item)
        L.append(value)
    except ValueError:
        if item.strip() == "":
            print("Chuỗi rỗng không hợp lệ, tự đổi thành '' ")
            L.append("")
        else:
            L.append(item)
print("\nList L đã nhập:", L)
hop_le = True
for i in range(len(L)):
    if i % 2 == 0:  # vị trí chẵn → phải là chuỗi
        if not isinstance(L[i], str):
            hop_le = False
            break
    else:           # vị trí lẻ → phải là số nguyên
        if not isinstance(L[i], int):
            hop_le = False
            break
if not hop_le:
    print("\nCác phần tử KHÔNG xen kẽ chuỗi – số!")
else:
    print("\n✔ Các phần tử xen kẽ chuỗi – số đúng dạng!")
    # Tạo list K theo yêu cầu
    # K[i/2] = L[i] * L[i+1]  (chỉ lấy i chẵn)
    K = []
    for i in range(0, len(L), 2):   # bước nhảy 2
        ket_qua = L[i] * L[i+1]
        K.append(ket_qua)
    print("List K tạo ra:", K)
