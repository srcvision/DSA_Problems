def pat13(n):
    for i in range(n):
        for j in range(i+1):
            print(chr(j+65),end=" ")
        print( )
n=int(input("Enter a number: "))
pat13(n)