# # atm programe
# amo=int(input("enter a bank amount = "))
# num = int(input("enter a atm pin = "))
# pin = int(input("enter a pin = "))

# if num == pin :
#     print( "'1' check bank balance")
#     print( "'2' bank deposite")
#     print( "'3' widhraw ")

#     number = int(input("enter a value under 1 to 3 = "))

#     if number == 1:
#         print(f"your current bank balance is ${amo}")
#     elif number ==2:
#         print(f"old bank balance = ${amo}")
#         amou=int(input("enter a amount for the deposite = "))
#         amo+=amou
#         print(f"new bank balance = ${amo}")
#     elif number == 3:
#         wid=int(input("enter a widhraw amount = "))
#         if wid <= amo:
#             amo-=wid
#             print(f"remaning bank balance is ${amo}")
     
#         else :
#             print("insufficient bank balance")
# else:
#     print("pin is invalid please enter a valid pin ")






# salary calculatio 


number = int(input("enter a salary amount = "))
if number > 100000 :
    per = int(input("emter a percentage = "))
    bonus = number * per / 100
    salary = bonus + number
    print(f" total salary of employee is ${salary}")
elif number > 250000:
    per = int(input("emter a percentage = "))
    bonus = number * per / 100
    salary = bonus + number
    print(f" total salary of employee is ${salary}")
else :
    print(f"you are not eligible for the bonus, so your current salary is {number}")
    