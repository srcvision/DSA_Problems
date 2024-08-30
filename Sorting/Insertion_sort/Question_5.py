# Question-5
# Sort even-placed elements in increasing and odd-placed in decreasing order
def inseration_sort(arr):
    n = len(arr)
    for i in range(1,n):
        key = arr[i]
        j=i-1
        while j>=0 and key < arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr
def even_odd_element(arr):
    inseration_sort(arr)
    even = []
    odd = []
    for i in range(len(arr)):
        if i%2==0:
            even.append(arr[i])
        else:
            odd.append(arr[i])
    return even,odd
arr = [1,2,3,4,5,6,7,8,9,10]
print(even_odd_element(arr))
    
    