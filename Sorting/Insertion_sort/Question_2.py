# Question-2
# Find the Second largest elements in an array
def inseration_sort(arr):
    n=len(arr)
    for i in range(1,n):
        key = arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr

def Second_largest_arr(arr):
    second_largest=inseration_sort(arr)
    second_largest = second_largest[::-1]
    print(second_largest)
    for i in range(1,len(second_largest)):
        if second_largest[i]!=second_largest[0]:
            print("The second largest Element is :",second_largest[i])
            return 
    print("There is no second largest Element")
    
arr=[1,1654,1,31,6,4,12,9,61,84,98,56,4]
Second_largest_arr(arr)        