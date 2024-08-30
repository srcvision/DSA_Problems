# Question-1
# Insertion sort problem
import random
def insertion_sort(arr):
    n=len(arr)
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key
    return arr
arr = [4,1,49,7,94,1,49,4,6,87,74,9,7,87,9]
print("Sorted arrays is:",insertion_sort(arr))