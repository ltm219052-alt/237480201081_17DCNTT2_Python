def nhap_dictionary():
    d = {}
    print("Nhập dictionary (nhập 'stop' để dừng):")
    while True:
        key = input("Nhập key: ")
        if key.lower() == "stop":
            break
        while True:
            try:
                value = int(input(f"Nhập giá trị cho key '{key}': "))
                break
            except ValueError:
                print("Giá trị phải là số nguyên! Nhập lại.")
        d[key] = value
    return d
def key_max_value(dic):
    if not dic:
        return None
    return max(dic, key=lambda k: dic[k])
data = nhap_dictionary()
print("Dictionary vừa nhập:", data)
kq = key_max_value(data)
print("➡ Key có giá trị lớn nhất là:", kq)
