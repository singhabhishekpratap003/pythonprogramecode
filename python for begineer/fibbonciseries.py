
#take a input from yhe user

n=int(input("enter a value of fibbonci series = "))

#declare the variable to store the value 

a=0
b=1

print("print fibbonci series")

for i in range(n):
    print(a,end=" ")
    z=a+b
    a=b
    b=z