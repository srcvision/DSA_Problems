# Question - 8
# Missing Element
def missing(nums):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == mid:
            left = mid + 1
        else:
            right = mid - 1

    return left
nums = [0, 1, 2, 4]
print("Missing number:", missing(nums))  
