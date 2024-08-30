# Quesion - 2
# find_most of time Reapeated Value in array using selection sort
def findRepeated(arr):
    n=len(arr)
    for i in range(n-1):
        mini=i
        for j in range(i-1,n):
            if arr[j]<arr[mini]:
                mini =j
                arr[i],arr[mini]=arr[mini],arr[i]
def minisum(arr):
        findRepeated(arr)
        duplicate=set()
        for i in range(1,len(arr)):
            if arr[i] == arr[i-1]:
                duplicate.add(arr[i])
                return duplicate
       
arr=[0,1,2,5646,5,646,6,16,549,6,59599,9,99,9,9,9,96,69,6,596,9,65,965,965,965,]
print("Sorted Array:",minisum(arr))