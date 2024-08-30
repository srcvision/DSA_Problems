# Time Complexitiy - O(n log n)
# Space Complexity - O(n)
def second(arr,n):
    arr.sort()
    second_maximum = arr[n-2]
    second_smallest = arr[1]
    return [second_maximum, second_smallest]
arr=[15,4,5,1,51,4,6,9,79,79,7]
n = len(arr)
result = second(arr,n)
print("second largest and smallest Worst-case:-",result)

# Write a code to find a second largest and second smallest element with in O(n) Time Complexity algorithm
# Time Complexitiy - O(n)
# Space Complexity - O(n)
def second_largest_smallest(arr,n):
    def second_largest1():
        num = float('-inf')
        second_largest = float('-inf')
        for i in range(0,n):
            if arr[i] > num:
                num = arr[i]
        for j in range(n):
            if arr[j] > second_largest and arr[j] != num:
                second_largest=arr[j]
        return second_largest

    def second_smallest():
        small = float('inf')
        second_smallest = float('inf')
        for i in range(0,n):
            if arr[i] < small:
                small=arr[i]
        for j in range(n):
            if arr[j] < second_smallest and arr[j] != small:
                second_smallest = arr[j]
        return second_smallest
    return [second_largest1(),second_smallest()]

arr = [15,4,1,4,41,6,48,4,3,6,9]
n = len(arr)
result = second_largest_smallest(arr,n)
print("second largest and smallest Best-Case:-\t",result)


