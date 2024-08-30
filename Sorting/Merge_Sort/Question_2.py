# Question - 2
# Maximum Length of subsequence 
# You are given an array A consisting of N integers. A subsequence of the array is
# called good if every pair of elements in the subsequence have an absolute
# difference of at most 10.
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
    print(new)
    return new


def maxs(arr):
    sorted_arr = merge_sort(arr)
    N = len(sorted_arr)
    sub = [1] * N

    for i in range(1, N):
        for j in range(i-1, -1, -1):
            if abs(sorted_arr[i] - sorted_arr[j]) <= 10:
                print(sorted_arr[i],end=" ")
               
                print("-",sorted_arr[j])

                sub[i] = max(sub[i], sub[j] + 1)
                #print(dp)

                

    return max(sub)
num = [3, 15, 7, 9, 12, 4, 8]
print("Maximum length of good subsequence:", maxs(num))
