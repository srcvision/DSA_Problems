def pat9(n):
    for i in range(1,n+1):
        space = n - i
        star = 2*i-1
        print(" "*space+'*'*star)
    for j in range(n,-1,-1):
        space = n-j
        star = 2*j-1
        print(" "*space+'*'*star)
n = int(input("Enter a number: "))
pat9(n)