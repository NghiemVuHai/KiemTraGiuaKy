def kiem_tra_so_nguyen_to(n):
    """
    Kiểm tra xem một số có phải là số nguyên tố hay không
    
    Args:
        n: Số nguyên dương cần kiểm tra
        
    Returns:
        True nếu n là số nguyên tố, False nếu không phải
    """
    # Số nguyên tố phải lớn hơn 1
    if n <= 1:
        return False
        
    # Kiểm tra từ 2 đến căn bậc hai của n
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
        
    return True

def main():
    try:
        n = int(input("Nhập vào một số nguyên dương n: "))
        if n <= 0:
            print("Vui lòng nhập số nguyên dương (lớn hơn 0).")
            return
            
        if kiem_tra_so_nguyen_to(n):
            print(f"{n} là số nguyên tố.")
        else:
            print(f"{n} không phải là số nguyên tố.")
    except ValueError:
        print("Vui lòng nhập một số nguyên hợp lệ.")

if __name__ == "__main__":
    main()