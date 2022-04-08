from SavingAccount import SavingAccount
from YouthAccount import YouthAccount
from Client import Client
from time import time

clientA = Client('Cyrill', 'Gurtner', 'Bahnhofstrasse 40', '1992-07-20')
print('====== TEST saA ======')
saA = SavingAccount(clientA)
saA.deposit(2000)
saA.deposit(200)
print(saA)

print()
print('====== TEST saAA ======')
saAA = SavingAccount(clientA)
saAA.deposit(2000)
saAA.deposit(200)
# this should withdraw 3060 because of 2% commission on too high withdraw
# balance should be -860 CHF
saAA.withdraw(3000)
print(saAA)

print()
print('====== TEST yaA ======')
clientB = Client('A', 'B', 'Bahnhofstrasse 40', '1992-07-20')
yaA = YouthAccount(clientB) 
# error message because account is immediatly closed on creation because of date of birth
yaA.deposit(200) 

print()
print('====== TEST yaB ======')
clientC = Client('A', 'B', 'Bahnhofstrasse 40', '2000-07-20')
yaB = YouthAccount(clientC)
yaB.deposit(2000)
yaB.deposit(200)
yaB.withdraw(200)
yaB.withdraw(400)
yaB.withdraw(1000)
# this should throw a message, because it would withdraw more than 2k in same month
# balance should remain 600.-
yaB.withdraw(500) 
print(yaB)

print()
print('We start the month-loop with:')
print(saA)
print(yaB)
print()

# simulate three months
t_start = time()
t_end = time() + 10 * 3
while t_end >= time():
    if abs(t_start - time()) % 10 == 0 or t_end - time() == 0:
        print('Monthly interest has been added!')
        saA.add_monthly_interest()
        yaB.add_monthly_interest()
        print()

print('After three months following changed:')
print(saA)
print(yaB)