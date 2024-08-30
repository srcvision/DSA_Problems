"""Question - 3
Remove a Duplicates from unsorted Array Using Merge _Sort"""
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
def duplicates(arr):
    sorted_arr = mergerr(arr)
    remove_arr = [sorted_arr[0]]

    for i in range(1, len(sorted_arr)):
        if sorted_arr[i] != sorted_arr[i - 1]:
            remove_arr.append(sorted_arr[i])

    return remove_arr

# Example usage:
arr = [3, 1, 2, 2, 4, 5, 4, 6]
remove_arr = duplicates(arr)
print("original :", arr)
print("Arrayremoving duplicates:", remove_arr)