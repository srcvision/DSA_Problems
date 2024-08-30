# Question - 7
# COunt Negative NUmber sorted matrix using binary search algorithm
def countNegatives(grid):
    count = 0

    for row in grid:
        count += binary_search(row)

    return count

def binary_search(row):
    left = 0
    right = len(row) - 1
    count = 0

    while left <= right:
        mid = left + (right - left) // 2

        if row[mid] < 0:
            count += right - mid + 1
            right = mid - 1
        else:
            left = mid + 1

    return count
matrix = [[-3, -2, -1, 1],[-2, 2, 3, 4],[4, 5, 7, 8]]
print(countNegatives(matrix))  
