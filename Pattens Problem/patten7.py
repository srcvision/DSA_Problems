# def pat7(n):
#     m=(2*n)/2
#     for i in range(n):
#         for j in range(int(m)):
#             print(end=" ")
#         m-=1
#         for k in range(i+1):
#             print("*",end=" ")
#         print( )
# n = int(input("entre a number: "))
# pat7(n)


def pat7(n):
    for i in range(n):
        space = n - i -1
        star = 2*i+ 1
        print(" "*space + "*"*star)
n = int(input("Enter a number: "))
pat7(n)
