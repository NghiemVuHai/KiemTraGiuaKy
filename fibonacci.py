def fibonacci_dp(n):
    """
    Tính số Fibonacci thứ n bằng quy hoạch động
    
    Args:
        n: Vị trí của số Fibonacci cần tính (n >= 0)
        
    Returns:
        Số Fibonacci thứ n
    """
    # Kiểm tra trường hợp cơ bản
    if n == 0:
        return 0
    if n == 1:
        return 1
        
    # Khởi tạo mảng để lưu các giá trị Fibonacci đã tính
    fib = [0] * (n + 1)
    fib[0] = 0
    fib[1] = 1
    
    # Tính các giá trị Fibonacci từ 2 đến n
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    
    return fib[n]

def main():
    try:
        n = int(input("Nhập vào số nguyên không âm n: "))
        if n < 0:
            print("Vui lòng nhập số nguyên không âm (n >= 0).")
            return
            
        result = fibonacci_dp(n)
        print(f"Số Fibonacci thứ {n} là: {result}")
        
    except ValueError:
        print("Vui lòng nhập một số nguyên hợp lệ.")

if __name__ == "__main__":
    main()