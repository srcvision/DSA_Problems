# Question - 3
# Find The Second Laregst Element
def selection_sort(arr):
    n=len(arr)
    for i in range(n-1):
        mini=i
        for j in range(i+1,n):
            if arr[j]<arr[mini]:
                mini=j
        arr[i],arr[mini]=arr[mini],arr[i]
    return arr

def second_largest(arr):
    arr=selection_sort(arr)
    sl = arr[::-1]
    for i in range(1,len(arr)):
        if sl[i] != sl[0]:

            return "Second Largest Element:",sl[i]
            
arr=[1,1654,1,31,6,4,12,9,61,84,98,56,4]
print(second_largest(arr)) 
        