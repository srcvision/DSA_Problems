# Question-6
# Find Duplicate in Array
def mergerr(N):
    if len(N)<=1:
        return N
    mid = len(N)//2
    l=N[:mid]
    r=N[mid:]
    l=mergerr(l)
    r=mergerr(r)
    return merg(l,r)
def merg(l,r):
    new=[]
    i,j=0,0
    while i<len(l) and j<len(r):
        if l[i]<r[j]:
            new.append(l[i])
            i+=1
        else:
            new.append(r[j])
            j+=1

    new.extend(l[i:])
    new.extend(r[j:])
    return new

def find_duplicates(arr):
    mergerr(arr)
    duplicates = set()
    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1]:
            duplicates.add(arr[i])
    return duplicates

arr = [4, 2, 7, 9, 2, 4, 5, 7, 3,2,2,2,2]
print("Duplicates:", find_duplicates(arr))
