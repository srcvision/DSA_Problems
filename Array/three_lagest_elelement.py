def lagest_three(arr):
    if len(arr) < 3:
        print ("Invalid lagest")
        return 
    first=second=third=float('-inf')
    for i in range(len(arr)):
        if arr[i]>first:
            third=second
            second=first
            first=arr[i]
        elif arr[i]>second and arr[i]!=first:
            third=second
            second=arr[i]
        elif arr[i]>third and arr[i]!=first and arr[i]!=second:
            third=arr[i]
    print(f"largest three elements first({first}), second({second}) and third({third}))")
arr = [49,4,41,94,16,4,1,64,1,49,5,49,6,1,64,95,95,9]
lagest_three(arr)