# MOve non -zero value in last position of given array

def move_non_zero(arr,n):
    temp = []
    nz= len(temp)
    for i in range(n):
        if arr[i] != 0:
            temp.append(arr[i])
    for j in range(nz):
        arr[j] = temp[j]
    
    return temp

def move_zeros(arr,n):
    j=-1
    for i in range(n):
        if arr[i] ==0:
            j = i
            break;
    for i in range(j+1):
        if arr[i]!=0:
            arr[i],arr[j+1] = arr[i],arr[j+1]
            return arr
                
    

arr = [2,4,0,4,2,0,6,1,2,8,0]
n = len(arr)
result = move_zeros(arr, n)
print("Updated result is: ", result)

            