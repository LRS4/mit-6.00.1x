"""
Bisection search:
Write a program to search for the smallest monthly payment such that we can pay off the entire balance within a year
"""

"""
Monthly interest rate = (Annual interest rate) / 12.0
Monthly payment lower bound = Balance / 12
Monthly payment upper bound = (Balance x (1 + Monthly interest rate)12) / 12.0
"""

balance = 320000
annualInterestRate = 0.2

init_balance = balance
monthlyInterestRate = annualInterestRate / 12
lower = init_balance/12
upper = (init_balance * (1 + monthlyInterestRate) ** 12) / 12.0
epsilon = 0.03

while abs(balance) > epsilon:
    monthlyPaymentRate = (upper + lower)/2
    balance = init_balance
    for i in range(12):
        balance = balance - monthlyPaymentRate + ((balance - monthlyPaymentRate) * monthlyInterestRate)
    if balance > epsilon:
        lower = monthlyPaymentRate
    elif balance < -epsilon:
        upper = monthlyPaymentRate
    else:
        break
        
print('Lowest Payment:', round(monthlyPaymentRate, 2))