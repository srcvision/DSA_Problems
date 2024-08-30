# Question - 4
# Given an array Arr of size N consisting of only 0's and 1's. The array is 
# sorted in such a manner that all the 1's are placed 
# first and then they are followed by all the 0's. Find the count of all the 0's.
def count_zeros(arr,target):
   
    left, right = 0, len(arr) -1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] == arr[right]:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def find_zeros(arr):
    dic = {}
    for i in arr:
        value = count_zeros(arr,i)
        for j in range(0,value):
            dic[arr[j]]=arr.count(arr[j])
    return dic

arr = [0,0,0,1,1,1]

print("Number of zeros in the array:", find_zeros(arr))


    