n=int(input('enter the number:'))
sum=0
product=1
for i in range(1,n+1):
    sum=sum+i
    product=product*i
print(f'sum of {n} numbers:{sum}\nproduct of {n} numbers:{product}')