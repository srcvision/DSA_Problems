def pat14(n):
    for i in range(n+1,-1,-1):
        for j in range(i-1):
            print(chr(j+65),end=" ")
        print( )
n=int(input("Enter a number: "))
pat14(n)