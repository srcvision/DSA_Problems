def pat5(n):
    for i in range(n+1,1,-1):
        for j in range(i-1):
            print("*",end=" ")
        print( )
n = int(input("entre a number: "))
pat5(n)