n=int(input("enter the number"))
if n%4==0 and n%100!=0 or n%400==0:
    print("it is a leap year")
else:
    print("it is not a leap year")    