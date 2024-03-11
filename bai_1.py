def openRussianDoll (doll):
    # Kiểm tra điều kiện dừng
    if doll == 1:
        print ("All dolls are opened")
    # Gọi đệ quy nếu điều kiện không thỏa mãn
    else:
        openRussianDoll (doll - 1)
# Sử dụng chương trình
openRussianDoll (4)