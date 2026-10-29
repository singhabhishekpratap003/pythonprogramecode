#find the factorial

n = int(input("enter a value = "))
fact = 1
for i in range(1 , n+1):
    fact = i*fact
    
print(fact)