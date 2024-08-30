"""Question - 5
Merge Sort decending Order unsorted Array Using Merge _Sort"""
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
        if l[i]>=r[j]:
            new.append(l[i])
            i+=1
        else:
            new.append(r[j])
            j+=1

    new.extend(l[i:])
    new.extend(r[j:])
    return new

arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_arr = mergerr(arr)
print("Sorted array in descending order:", sorted_arr)
