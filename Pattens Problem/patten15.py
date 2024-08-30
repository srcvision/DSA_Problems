def pat15(n):
    for i in range(n+1):
        for j in range(i+1):
            print(j,end=" ")
        print( )
n=int(input("Enter a number: "))
pat15(n)