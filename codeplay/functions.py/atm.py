data = {
    'balance' : 50000,
    'transaction' : []}

def withdraw(amt):
    if amt <= data['balance']:
        data['balance'] -= amt
        data['transaction'].append(f'{amt} withdrawn from your account.')
        print("Amount is succesfully withdrawn.")
    else:
        print("Insufficient balance")

def deposit(amt):
    data['balance'] += amt 
    data['transaction'].append(f'{amt} deposited to your account.')
    print("Amount is succesfully deposited.")
    
def checkbalance():
    print(f"Your current balance is {data['balance']}")

    
def viewtransaction():
    for i in data['transaction']:
        print(i)

print("welcome to ATM")

while True:
    print('1.Withdraw')
    print('2.Deposit')
    print('3.Checkbalance')
    print('4.Viewtransaction')
    print('5.Exit')
    
    op = int(input('enter the selection(1,5): '))


    if op == 1:
        amt = int(input("enter the amount you want to withdraw: "))
        withdraw(amt)
    
    elif op == 2:
        amt = int(input("enter the amount you want to deposit: "))
        deposit(amt)
    
    elif op == 3:
        checkbalance()

    elif op == 4:
        viewtransaction()
    
    elif op == 5:
        print("See you later")
        break
    else:
        print("Try Again")