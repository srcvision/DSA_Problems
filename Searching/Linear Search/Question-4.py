# Question - 4
# Given three arrays sorted in increasing order. Find the elements that are common in all three arrays.
# Note: can you take care of the duplicates without using any additional Data Structure?
def common_elements(a,b,c,n1,n2,n3):
    arr=set()
    for i in range(n1):
        for j in range(n2):
            for k in range(n3):
                if a[i]==b[j] and b[j]==c[k]:
                    arr.add(a[i])
                    arr.add(b[j])
                    arr.add(c[k])
    return arr
a=[1,2,3,4,5,6,7,8,9,10]
b = [2,3,6,8]
c = [ 1, 2, 6]
n1=len(a)
n2=len(b)
n3=len(c)
print("Common Element is :",common_elements(a,b,c,n1,n2,n3))