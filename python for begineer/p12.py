# # # check the number is divisible by 5 and 11
# # # number = int(input("enter a value = "))

# # # if number%5==0 and number%11==0:
# # #     print(f"this number {number} is divisible by both 5 and 11 ")
# # # else:
# # #     print("out of range")

# # # check character is alphabet or not

# # ch = input("Enter a character: ")

# # if ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):
# #     print("Alphabet")
# # else:
# #     print("Not an alphabet")


# ch = input("enter a value = ")

# if ( 'a' <= ch  <= 'z'):
#     print("lower case")
# elif ( 'A' <= ch <= 'Z'):
#     print(" upper case")
# else:
#     print(" out of range")

# find electricity bill 

num = int(input(" enter a value = "))
numb = int(input("enter a value = "))

if 0 < num < 100 :
    print(f"electricty bill is = { num*numb}")
elif 100 < num < 300:
    print(f"electricity bill is = {num * numb +100} plus $100 fine")
elif 300 < num < 500:
    print(f"electricity bill is = {num * numb +300} plus $300 fine")
else :
    print(f"electricity bill is = { num*numb+1000} plus $1000 fine")
