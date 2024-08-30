# Question -2
# Sort the array and find the element using binary search
def inserations_sort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return i
   # temp =  ''.join(list(map(str, selection_sort(list(map(int, list(str(num))))))))

def binary_search(arr,left,right,target):
    inserations_sort(arr)
    while left<=right:
        mid = left+(right-left)//2
        if arr[mid] == target:
            return mid
        elif arr[mid]<target:
            left = mid+1
        else:
            right =mid-1
    return -1
arr = [65,56,4,4,9,9,61,61,6,46,16,46,4,6,9]
target= 46
left=0
right = len(arr)-1
result= binary_search(arr,left,right,target)
print("Ans:",result)
    
            
