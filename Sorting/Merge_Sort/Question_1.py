# Question - 1
# Turbo Sort
# Given a list of numbers, you have to sort them in non decreasing order.dublicate value not in sorted array
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
N = list(map(int,input("Enter Value Here:-").split()))
N = list(set(N)) 
new=mergerr(N)
print("Sorted Array:",new)
    