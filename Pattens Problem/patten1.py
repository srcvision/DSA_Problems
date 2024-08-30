def pat1(n):
    for i in range(n):
        for j in range(n):
            print('*',end=' ')
        print("")
          
n = int(input("Enter the number: "))
pat1(n)