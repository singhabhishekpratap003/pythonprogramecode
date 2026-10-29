# print even numbers

num = int(input("enter a value = "))
sum = 0
for i in range(num):
    if i%2==0:
        sum = sum+i
print(sum)
