"""
Now write a program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months."""

"""
Monthly interest rate = (Annual interest rate) / 12.0
Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
"""

balance = 3329
annualInterestRate = 0.2
init_balance = balance
monthlyInterestRate = annualInterestRate / 12.0
monthlyPayment = 0

while balance > 0:
    for i in range(12):
        balance = balance - monthlyPayment + ((balance - monthlyPayment) * monthlyInterestRate)
    if balance > 0:
        monthlyPayment += 10
        balance = init_balance
    elif balance <= 0:
        break

print('Lowest Payment:', monthlyPayment)