def calculate(price,rate,time):
    sum=(price*rate*time)/100
    return(sum)
price=float(input("enter the price"))
rate=float(input("enter the rate"))
time=float(input("enter the time"))
simple_interest=calculate(price,rate,time)
print(simple_interest)