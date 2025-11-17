print("Bấm 0 để thoát!")
while True:
    try:
        n = int(input("Nhập số lượng phần tử: "))
        break
    except ValueError:
        print("Nhập số bất kỳ!")

sv = []
for i in range(n):
    name = input(f"Nhập tên sinh viên thứ {i+1}: ")
    sv.append(name)

while True:
    tim = input("Nhập tên sinh viên cần tìm (nhập 0 để dừng): ")

    if tim == "0":
        print("Kết thúc tìm kiếm!")
        break

    found = False
    for ten in sv:
        if ten.lower() == tim.lower():
            found = True
            break

    if found:
        print("=> Sinh viên có trong danh sách!")
    else:
        print("=> Không tìm thấy sinh viên!")