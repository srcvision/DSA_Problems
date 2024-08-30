# Time Complexity : O(n)
# Space Complexity : O(1)
def rotate_left(arr,n):
    temp=arr[0]
    for i in range(1,n):
        arr[i-1] = arr[i]
    arr[n-1] = temp
    return arr


# left rotate the array by d places
def rotate_left_d(arr,n,d):
    for i in range(d):
        temp=arr[0]
        for j in range(n-1):
            arr[j] = arr[j+1]
        arr[n-1]=temp
    return arr



# right rotate the array by d places
def rotate_right_d(arr,n,d):
    for i in range(n-1):
        a = arr[i-d:]
        b = arr[:i-d]
        marge  = a+b
        return marge
    
def rotate_left_da(arr,n,d):
    for i in range(n-1):
        a = arr[i+d:]
        b = arr[:i+d]
        marge = a+b
        return marge
arr= [1,2,3,4,5,6,7]
n=len(arr)
d=5
result = rotate_left_da(arr,n,d)
print("Updated array is: ", result)        
        
    