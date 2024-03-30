def max_so_luong_nguyen_lieu(U, V, A, B):
    max_so_luong = 0
    
    for a in A:
        for b in B:
            max_so_luong = max(max_so_luong, min(U / a, V / b))
    
    return max_so_luong

U = float(input("Nhập số tiền U (USD): "))
V = float(input("Nhập số tiền V (Euro): "))
A = list(map(float, input("Nhập list giá bán Ai (USD/kg): ").split()))
B = list(map(float, input("Nhập list giá bán Bi (Euro/kg): ").split()))

result = max_so_luong_nguyen_lieu(U, V, A, B)
print("Số lượng nguyên liệu mua được là: {:.2f} kg".format(result))


