# Question - 9
# Find How many time number are repeated in array
def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        mini = i
        for j in range(i-1, n):
            if arr[j]<arr[mini]:
                mini = j
                arr[i],arr[mini]=arr[mini],arr[i]
                
def findReapeted(arr,target):
    
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
def find_occurrance(arr):
    dic = {}
    selection_sort(arr)
    for i in arr:
        value = findReapeted(arr,i)
        
        for j in range(0,value):
            dic[arr[j]]=arr.count(arr[j])
    return dic

arr=[0,1,2,5,6,8,4,2,3,6,5,1,4,5,2,5,8]
print("All Occurrance",find_occurrance(arr)) 
"""counti={}
for i in range(n):
    counti[arr[i]]=arr.count(arr[i])
print(counti)"""
"""for num in arr:
        first_index = selection_sort(arr,num)
        if first_index != -1:
            occurrences[num] = arr.count(num)"""