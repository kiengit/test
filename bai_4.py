def powerOfTwo (n):
    # Kiểm tra điều kiện dừng
    if n == 0:
        return 1
    else:
        # Gọi đệ quy và lưu giá trị trả về vào biến power
        power = powerOfTwo (n - 1)
        # Trả về kết quả là power * 2
        return power * 2
# Gọi hàm với tham số là 3
a = powerOfTwo (3)
print (a)