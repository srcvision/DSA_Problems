def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr)//2
    l=arr[:mid]
    r=arr[mid:]
    left = merge_sort(l)
    right = merge_sort(r)

    return merge(left, right)

def merge(left, right):
    new = []
    i,j = 0,0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            new.append(left[i])
            i += 1
        else:
            new.append(right[j])
            j +=1

    new.extend(left[i:])
    new.extend(right[j:])
    return new

def maxs(points):
    coordinates = [point[0] for point in points]
    sorted=merge_sort(coordinates)
    print(sorted)

    max_width = 0
    for i in range(1, len(sorted)):
        max_width = max(max_width, sorted[i] - sorted[i - 1])
        print(sorted[i],sorted[i-1])
    return max_width
points = [[8,7],[9,9],[7,4],[9,7]]
print("Widest vertical area:", maxs(points))
