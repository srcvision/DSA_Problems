# Question - 10
# find element in list who has a even or odd element using binary search
def string_search(arr,target):
    left,right = 0,len(arr)-1
    while left<=right:
        mid = left+(right-left)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            left = mid +1
        else:
            right = mid-1
    return-1
def even_target(arr,target):
    dic = {}
    
    value = string_search(arr,target)
    if value%2==0:
        dic[arr[value]]="Even Number"
    else:
        dic[arr[value]]='Odd Number'
    return dic
arr=[0,1,2,3,4,5,6,7,8,9,10]
target = input("entre your target:")
print("All Occurrance",even_target(arr,int(target))) 
        
            

        
        
        