# Định nghĩa hàm
def firstMethod ():
    # Gọi hàm
    secondMethod ()
    #in ra thông điệp
    print ("I am the first Method")

def secondMethod ():
    # Gọi hàm
    thirdMethod ()
    #in ra thông điệp
    print ("I am the second Method")

def thirdMethod ():
    # Gọi hàm
    fourthMethod ()
    #in ra thông điệp
    print ("I am the third Method")

def fourthMethod ():
    #in ra thông điệp
    print ("I am the fourth Method")
# Gọi hàm đầu tiên để bắt đầu chuỗi các lời gọi hàm
firstMethod ()