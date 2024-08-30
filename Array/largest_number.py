# Time Complexity:- O(n log n)
# Space Complexity:- O(n)
def largest(arr,n):
    arr.sort()
    num = arr[-1]
    return num
        
# Time Complexity = O(n)
# Space Complexity = O(n)
def largest2(arr,n):
    num = float('-inf')
    for i in range(n):
        if arr[i]>num:
            num = arr[i]    
    return num

arr = [20,5,0,7,8,6,3]
n = len(arr)
a = largest(arr,n)
c = largest2(arr,n)
print("Largest element is Worest(O(nlogn)):- ",a)
print("Largest element is Best(O(n)):- ",c)