def rotote(arr,d):
    n = len(arr)
    for i in range(d):
        first = arr[0]
        for j in range(n-1):
            arr[j]=arr[j+1]
        arr[n-1]=first

arr = [1, 2, 3, 4, 5]
d = 2
rotote(arr, d)
print("Rotated array is:", arr)