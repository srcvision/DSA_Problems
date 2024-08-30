# Question -1 
# Find Duplicate in Array using selection sort
def selection_sort(arr):
    n=len(arr)
    for i in range(n-1):
        mini=i
        for j in range(i+1,n):
            if arr[j]<arr[mini]:
                mini=j  
                arr[i],arr[mini]=arr[mini],arr[i]
    return arr
        
def tempMinSum(num):
    temp =  ''.join(list(map(str, selection_sort(list(map(int, list(str(num))))))))
    return int(temp[0] + temp[2]) + int(temp[1] + temp[3])

num = 7894
print("Minimum possible sum is:", tempMinSum(num)) 

'''def minSum(num):
    digits = [int(d) for d in str(num)]
    pairs = []
    for i in range(1, len(digits)):
        new1 = int(''.join(map(str, digits[:i])))
        new2 = int(''.join(map(str, digits[i:])))
        print(new1,new2)
        pairs.append(new1 + new2)
    selection_sort(pairs)
    return pairs[0]'''
