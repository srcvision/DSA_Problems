# Question-1
# Normal Binary Search Code
def binarysearch(arr,left,right,x):
    while left<=right:
        mid = left+(right - left)//2
        print(arr[left], " :: ", arr[right], " :: ", arr[mid])
        if arr[mid]==x:
            return mid
        elif arr[mid]<x:
            left = mid+1
        else:
            right =  mid-1
    return -1
arr = [2,35,6,565,5,6000,526,526,25,652,5,6]
arr.sort()
print(arr)
x = 652
l=0
r=len(arr)-1
result = binarysearch(arr,l,r,x)
print("Binry Search Result is:",result)