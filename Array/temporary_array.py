def rotate(arr,d):
    n = len(arr)
    l=[]
    l=arr[d:]+arr[0:d]
    return l

arr = [1,2,3,4,5,6,7,8,9]
d = 2
a = rotate(arr, d)
print("Rotated array is:", a)