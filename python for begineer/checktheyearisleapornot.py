year = int(input("enter a year = "))
if (year % 4==0 and year% 100 !=0) or (year %400 ==0) :
    print("this year is leap year = ", year)
    print("thank you")
else:
    
    print("yhos year is not a leap year = ", year)