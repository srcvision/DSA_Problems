# Question - 4
# Move all zeroes to end of array
#     Given an array of random numbers, Push all the zero’s of a given array to the 
# end of the array. For example, if the given arrays is {1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0},
# it should be changed to {1, 9, 8, 4, 2, 7, 6, 0, 0, 0, 0}. The order of all other elements
# should be same. Expected time complexity is O(n) and extra space is O(1).
def inseration_sort(arr):
    n = len(arr)
    for i in range(1,n):
        key = arr[i]
        j=i-1
        while j>=0 and key < arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr
def move_all_zeros(arr):
    arr = inseration_sort(arr)
    zero = 0
    n = len(arr)
    for i in range(n):
        if arr[i] !=0:
            print(arr[i])
            arr[zero],arr[i] = arr[i],arr[zero]
            zero+=1
            print(arr)
    return arr
 
arr = [1,9,8,4,0,0,2,7,0,6,0]
print("The Final Ans is:",move_all_zeros(arr))