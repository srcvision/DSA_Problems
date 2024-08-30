# Time Complexitiy - O(n log n)
# Space Complexity - O(n)
def dublicate(arr,n):
    dub  =  set(arr)
    return dub


def Dublicate(arr,n):
    for i in range(n):
        for j in range(i+1):
            if arr[i] !=arr[j]:
                dub = arr[i]
                return [dub]
arr = [64,1,1,1,4,6,316,1,65,6,6,66,6,1]
n=len(arr)
result = Dublicate(arr,n)
print("Remove Dublicate Best-Case:-\t",result)
                