def chuoi_ngan_nhat(lst):
    return min(lst, key=len)
def nhap_list_chuoi():
    s = input("Nhập các chuỗi (cách nhau bằng dấu cách): ")
    return s.split()
L = nhap_list_chuoi()
print("Chuỗi ngắn nhất là:", chuoi_ngan_nhat(L))
