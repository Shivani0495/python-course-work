def num(a,b):
    a.append(b)
    print(a)
a=list(map(int,input("enter the numbers:").split())) 
b=int(input("enter the number:"))
num(a,b)   