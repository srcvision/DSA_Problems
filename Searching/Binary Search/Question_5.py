# Question -5
# Finding the Minimum Element
def selection_sort(arr):
    n=len(arr)
    for i in range(n-1):
        mini=i
        for j in range(i+1,n):
            if arr[j]<arr[mini]:
                mini=j
        arr[i],arr[mini]=arr[mini],arr[i]
    return arr
def minimum_element(arr):
    selection_sort(arr)
    left=0
    right=len(arr)-1
    while left<=right:
        mid = left + (right - left) // 2
       
        if arr[mid]== arr[right]:
            left = mid + 1
        elif arr[mid]==arr:
            return mid
        else:
            right = mid
    return left
    
arr = [5, 6, 7, 2,1, 3, 4]
print("Minimum:", minimum_element(arr))