# Question-2
# Sort the array and find the element using Linear Search algorithm 
def selection_sort(arr):
    n=len(arr)
    for i in range(n-1):
        mini = i
        for j in range(i+1, n):
            if arr[j]<arr[mini]:
                mini = j
            arr[i],arr[mini] = arr[mini],arr[i]
        
def find_element(arr,target):
    selection_sort(arr)
  
    for i in range(0,len(arr)):
        if arr[i] == target:
            return i
    return -1
arr = [6,6,66,6,6,6,6,6,1,61,61,61,1654,9,1,1]
target = 9
print("index number is:",find_element(arr,target))

