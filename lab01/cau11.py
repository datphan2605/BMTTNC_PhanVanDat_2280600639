def tinh_tong_so_chan(Ist) :
    tong = 0
    for num in Ist:
        if num % 2 == 0:
            tong += num
    return tong

# Nhập danh sách từ người dùng và xử lý chuỗi
input_list = input("Nhập danh sách các số, cách nhau bằng dấu phẩy: ")
numbers = list(map(int, input_list. split(',')))

# Sử dụng hàm và in kết quả
tong_chan = tinh_tong_so_chan(numbers)
print ("Tổng các số chẵn trong List là:", tong_chan)
