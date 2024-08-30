def pat12(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end=" ")
        space = (n-i)*2
        print(" "*space,end=" ")
        for m in range(i,0,-1):
            print(m,end = " ")
        print( )
n=input("enter a number: ")
pat12(int(n))

