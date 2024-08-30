# Question-3
# Find the largest three distinct elements in an array
def insertion_sort(arr):
    n=len(arr)
    for i in range(1,n):
        key = arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr
def find_largest_three(arr):
    arr = insertion_sort(arr)
    arr = arr[::-1]
    return arr[0], arr[1], arr[2]

arr =[555,548,8,1566,41,684,68,46]
arr = find_largest_three(arr)

print(arr)
    