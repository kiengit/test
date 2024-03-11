def recursiveMethod (n):
    # Kiểm tra nếu n nhỏ hơn 1
    if n < 1:
        print ("n is less than 1")
    else:
        # Gọi lại chính hàm với tham số n - 1 (đệ quy)
        recursiveMethod (n - 1)
        # In giá trị của n
        print (n)
# Gọi hàm với tham số là 4
recursiveMethod (4)