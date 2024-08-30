
# finding the key form array it exitising in array then return value
def finding(arr,k):
    n=len(arr)
    for i in range(n):
        if arr[i] == k:
            return i
arr = [10,50,40,60,70,80]
k = 60
result = finding(arr, k)
print("found position is:", result) 


# Put the value on user given index 
def put_value_at_position(arr,n,pos,value):
    if pos < 0 or pos > n:
        print("Invalid position!")
        return arr
    arr.insert(pos, value)
    return arr

arr = [10, 50, 40, 60, 70, 80]
print(f'original array:%s \n' % arr)
x = int(input("Entre a Value to put in array:"))
pos = int(input("Entre a Position to put a value in array:"))
result = put_value_at_position(arr, len(arr), pos, x)
print("Updated array is:", result)


# Deleting a value from the array at position
def delete_position_value(arr, pos):
    if pos < 0 or pos >= len(arr):
        print("Invalid position!")
        return arr
    del arr[pos]
    return arr
arr = [10, 50, 40, 60, 70, 80]
print(f'original array:%s \n' % arr)
pos = int(input("Entre a Position to put a value in array:"))
result = delete_position_value(arr, pos)
print("Updated array is:", result)