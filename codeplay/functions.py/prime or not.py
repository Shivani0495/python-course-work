def prime(num):
    for i in range(2,(num//2)+1):
        if num%1==0:
            return False
        return True
n=int(input('enter the number:'))
if prime(n):
    print('prime number')
else:
    print('not a prime number')        

  