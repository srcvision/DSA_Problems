def missingNumbers(arr, brr):
    # Write your code here
    c1 = {}
    c2 = {}
    missing = []
    
    for i in arr:
        c1[i] = c1.get(i, 0) + 1
    
    for j in brr:
        c2[j] = c2.get(j, 0) + 1
    for k in c2:
        if k not in c1 or c2[k] > c1[k]:
            missing.append(k)
    missing.sort()
    
    return missing

arr = [203, 204, 205, 206, 207, 208, 203, 204, 205, 206]
brr = [203, 204, 204, 205, 206, 207, 205, 208, 203, 206, 205, 206, 204]

missing = missingNumbers(arr, brr)
print("Missing elements:", missing)
