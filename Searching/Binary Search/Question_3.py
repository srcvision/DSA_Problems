# Question-3
# Given an integer x, find the square root of x. If x is not a perfect square, 
# then return floor(√x).
def floorSqrt(x): 
    if x == 0 or x == 1:
        return x
    left = 0
    right = x
    while left <= right:
        mid = left + (right - left) // 2
        if mid * mid > x:
            right = mid - 1
        elif mid * mid < x:
            left = mid + 1
        else:
            return mid
    return left

x = 9
print("The x is",x,"And Floorsqrt is: ",floorSqrt(x))
