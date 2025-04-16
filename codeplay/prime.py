n=int(input('enter the number:'))
prime=0
for i in range(2,(n//2)+1):
    if n%i==0:
        prime+=1
        break
if prime==0:
    print(n,'is prime number') 
else:
    print(n,'is not prime number')      
