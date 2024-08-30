def pat10(n: int) -> None:
    for i in range(n):
        for j in range(i+1):
            print('*',end="")
        print( )
    for k in range(n,1,-1):
        for n in range(k-1):
            print('*',end="")
        print( )
n = input("entre a number: ")
pat10(int(n))