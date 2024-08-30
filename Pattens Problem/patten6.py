def pat6(n):
    for i in range(n+1,1,-1):
        for j in range(i-1):
            print(j+1,end=" ")
        print( )
    
n=int(input('enter the number: '))
pat6(n)