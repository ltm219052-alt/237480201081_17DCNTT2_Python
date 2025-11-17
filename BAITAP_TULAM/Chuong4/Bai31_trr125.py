def key_max_value(d):
    max_key = None
    max_value = None

    for key, value in d.items():
        if (max_value is None) or (value > max_value):
            max_value = value
            max_key = key

    return max_key

'''d = {
    "a": 10,
    "b": 25,
    "c": 7,
    "d": 25
}

print("Key có giá trị lớn nhất:", key_max_value(d))'''
d = {}
while True:
    try:
        n = int(input("Nhập số lượng phần tử của dictionary: "))
        break
    except ValueError:
        print("Nhập số bất kỳ!")

for i in range(n):
    key = input(f"Nhập key thứ {i+1}: ")
    while True:
        try:
            value = int(input(f"Nhập value của '{key}': "))
            break
        except ValueError:
            print("Nhập số bất kỳ!")

    d[key] = value

print("Dictionary vừa nhập:", d)
print("Key có giá trị lớn nhất là:", key_max_value(d))
