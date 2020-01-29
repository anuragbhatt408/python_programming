x= int(input("enter the year : "))

if x%4==0 and x%100 !=0 or x%400==0 :
    print("{} year is leap year".format(x))
else:
    print("{} year is not leap year".format(x))
