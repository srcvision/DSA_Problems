# Question -6 
# negative index's
def last_negative_index(arr):
    left, right = 0, len(arr) - 1
        
    while left <= right:
        mid = left + (right - left) // 2
            
        if arr[mid] <= 0:
            left = mid + 1
        else:
            if mid == 0 or arr[mid - 1] <= 0:
                return mid
            right = mid - 1
    return -1 
arr = [-5, -3,-1, 0, 1, 2, 4, 8]
print(last_negative_index(arr))