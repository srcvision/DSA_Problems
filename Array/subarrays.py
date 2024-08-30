# Subarray using recursion 
def subarray_sum(arr, start, end):
    if end == len(arr):
        return 
    elif start > end:
        return subarray_sum(arr, 0,end+1)
    else:
        print("Subarrays: ",arr[start:end+1])
        return subarray_sum(arr, start+1, end)
arr = [1,2,3]
subarray_sum(arr, 0, 0)
    