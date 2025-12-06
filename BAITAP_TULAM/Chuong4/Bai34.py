def hoan_doi_dictionary(D):
    D_moi = {}   # dictionary sau khi hoán đổi
    for key, value in D.items():
        # Nếu value đã tồn tại trong D_moi → bị trùng key sau khi hoán đổi
        if value in D_moi:
            return None
        D_moi[value] = key  # hoán đổi key và value
    return D_moi
# ---- Chạy thử ----
data1 = {"a": 1, "b": 2, "c": 3}
data2 = {"x": 10, "y": 10, "z": 20}
print("Kết quả 1:", hoan_doi_dictionary(data1))  # hợp lệ
print("Kết quả 2:", hoan_doi_dictionary(data2))  # None vì trùng
