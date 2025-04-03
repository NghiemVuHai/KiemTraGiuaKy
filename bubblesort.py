def bubble_sort(arr):
    """
    Sắp xếp mảng theo thứ tự tăng dần bằng thuật toán Bubble Sort
    
    Args:
        arr: Mảng các số nguyên cần sắp xếp
        
    Returns:
        Mảng đã được sắp xếp theo thứ tự tăng dần
    """
    n = len(arr)
    
    # Lặp qua tất cả các phần tử trong mảng
    for i in range(n):
        # Cờ kiểm tra xem có hoán đổi phần tử nào trong vòng lặp hiện tại không
        swapped = False
        
        # Lặp qua các phần tử từ 0 đến n-i-1
        # Sau mỗi vòng lặp, phần tử lớn nhất đã được đưa về cuối mảng
        for j in range(0, n-i-1):
            # So sánh phần tử hiện tại với phần tử tiếp theo
            if arr[j] > arr[j+1]:
                # Hoán đổi nếu phần tử hiện tại lớn hơn phần tử tiếp theo
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
                
        # Nếu không có hoán đổi nào trong vòng lặp hiện tại,
        # tức là mảng đã được sắp xếp, thoát khỏi vòng lặp
        if not swapped:
            break
            
    return arr

def main():
    try:
        # Nhập mảng từ người dùng
        input_str = input("Nhập vào các số nguyên, cách nhau bởi dấu cách: ")
        arr = [int(x) for x in input_str.split()]
        
        if not arr:
            print("Mảng trống!")
            return
            
        # Sắp xếp mảng
        sorted_arr = bubble_sort(arr.copy())
        
        # In kết quả
        print("Mảng trước khi sắp xếp:", arr)
        print("Mảng sau khi sắp xếp:", sorted_arr)
        
    except ValueError:
        print("Vui lòng nhập các số nguyên hợp lệ.")

if __name__ == "__main__":
    main()