def linear_search(arr,x):
    for i in range(len(arr)):
        if arr[i]==x:
            return i
    return -1
arr = [61,6,16,49,49,4,6,46,4,9]
x = 4
result = linear_search(arr,x)
print("Result is ",result)