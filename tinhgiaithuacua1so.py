
def tinh_giai_thua(n):
    """
    Tính giai thừa của một số nguyên không âm
    
    Args:
        n: Số nguyên không âm
        
    Returns:
        Giai thừa của n (n!)
    """
    # Giai thừa của 0 là 1
    if n == 0:
        return 1
        
    # Tính giai thừa theo công thức n! = n × (n-1) × ... × 1
    ket_qua = 1
    for i in range(1, n + 1):
        ket_qua *= i
        
    return ket_qua

def main():
    try:
        n = int(input("Nhập vào một số nguyên không âm nnn: "))
        if n < 0:
            print("Vui lòng nhập số nguyên không âm (lớn hơn hoặc bằng 0).")
            return
            
        giai_thua = tinh_giai_thua(n)
        print(f"{n}! = {giai_thua}")
    except ValueError:
        print("Vui lòng nhập một số nguyên hợp lệ.")

if __name__ == "__main__":
    main()