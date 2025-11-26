import string

mat_khau = input("Nhập mật khẩu: ")

co_in_hoa = False
co_in_thuong = False
co_so = False
co_ky_tu_dac_biet = False

# Duyệt từng ký tự trong mật khẩu
for c in mat_khau:
    if c.isupper():
        co_in_hoa = True
    elif c.islower():
        co_in_thuong = True
    elif c.isdigit():
        co_so = True
    elif c in string.punctuation:
        co_ky_tu_dac_biet = True

do_dai_hop_le = len(mat_khau) > 6

if co_in_hoa and co_in_thuong and co_so and co_ky_tu_dac_biet and do_dai_hop_le:
    print("Mật khẩu mạnh")
else:
    print("Mật khẩu yếu")
