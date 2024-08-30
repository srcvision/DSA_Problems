
# Using inbuilt function
def reverse_array(arr):
    reversed_array = arr[::-1]
    return reversed_array
arr = [1,2,3,4,5,6]
a = reverse_array(arr)
print("Reverssed :",a)

# Using slicing
def reverse_array1(arr,start,end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
reverse_array1(arr, 0, 5)
print("Reversed list is")
print(arr)


arr = [0, 1, 2, 3, 4, 5, 6]
reverse = list(reversed(arr))
print("Reversed list using inbuilt function is",reverse)


def recursion_reversed(arr,start,end):
    if start>=end:
        return -1
    
    arr[start], arr[end] = arr[end], arr[start]
    recursion_reversed(arr, start+1, end-1)
arr = [1,2,3,4,5,6]
recursion_reversed(arr, 0, 5)
print("Reversed list is")
print(arr)
    

