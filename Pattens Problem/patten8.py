def pat8(n):
    for i in range(n,-1,-1):
        space = n - i
        star = 2*i-1
        print(" "*space+"*"*star)
n = int(input("Enter a number: "))
pat8(n)