from SavingAccount import SavingAccount
from YouthAccount import YouthAccount
from Client import Client
from time import time, sleep

clientA = Client('Cyrill', 'Gurtner', 'Bahnhofstrasse 40', '1992-07-20')
saA = SavingAccount(clientA)
saA.deposit(2000)
saA.deposit(200)
saA.pay_monthly_interest()
saA.print_balance()

clientB = Client('A', 'B', 'Bahnhofstrasse 40', '1992-07-20')
yaB = YouthAccount(clientB)
yaB.deposit(2000)

clientC = Client('A', 'B', 'Bahnhofstrasse 40', '2000-07-20')
yaC = YouthAccount(clientC)
yaC.deposit(2000)
yaC.deposit(200)
yaC.withdraw(200)
yaC.withdraw(400)
yaC.withdraw(1000)
yaC.withdraw(500)

print('We start the month-loop with:')
print(saA)
print(yaB)
print(yaC)
print()

# simulate three months
t_start = time()
t_end = time() + 10 * 3
while t_end >= time():
    if abs(t_start - time()) % 10 == 0 or t_end - time() == 0:
        print('Monthly interest has been payed!')
        saA.pay_monthly_interest()
        yaB.pay_monthly_interest()
        yaC.pay_monthly_interest()
        print()

print('After three months following changed:')
print(saA)
print(yaB)
print(yaC)