# Question - 5
# Count zeros in a array
def countzeros(arr,n):
    count = 0
    for i in range(n):
        if arr[i] == 0:
            count += 1
    return count

arr = [4,0,9,908,9,60609,9,0,0,0,0]
n = len(arr)
print("Total count is :",countzeros(arr,n))