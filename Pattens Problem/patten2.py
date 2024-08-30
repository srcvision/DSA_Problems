def pat2(n):
    for i in range(n):
        for j in range(i+1):
            print("*",end=" ")
        print( )
n = int(input("entre a number: "))
pat2(n)