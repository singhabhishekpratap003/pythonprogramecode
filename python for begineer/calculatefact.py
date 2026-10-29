n=int(input("enter a number for the factorial = "))
fact=1
for i in range(1,n+1):
    fact*=i
print(f"total factolial of this number {n} is = ", fact)