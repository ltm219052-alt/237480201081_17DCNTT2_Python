def nhap_dictionary():
    d = {}
    print("Nhập dictionary (nhập 'stop' để dừng):")
    while True:
        key = input("Nhập key (chuỗi): ")
        if key.lower() == "stop":
            break
        if key.strip() == "":# Kiểm tra key phải là chuỗi không rỗng
            print("Key không được để trống!")
            continue
        value = input(f"Nhập value cho key '{key}': ")# Nhập value (không bắt buộc kiểu, tùy bài yêu cầu)
        d[key] = value
    return d
def gia_tri_key_dai_nhat(dic):
    if not dic:
        return None
    key_max_len = max(dic, key=lambda k: len(k))# Tìm key dài nhất
    return dic[key_max_len]
data = nhap_dictionary()
print("Dictionary vừa nhập:", data)
kq = gia_tri_key_dai_nhat(data)
print("➡ Giá trị của key có độ dài lớn nhất là:", kq)
