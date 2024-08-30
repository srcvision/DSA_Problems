def pat4(n):
    for i in range(n):
        for j in range(i+1):
            print(i+1,end=" ")
        print( )
n = int(input("entre a number: "))
pat4(n)