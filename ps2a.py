"""
Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month.
"""

"""
Monthly interest rate= (Annual interest rate) / 12.0
Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
"""

balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
monthlyInterestRate = annualInterestRate / 12.0

month = 1
for i in range(12):
    balance += balance * monthlyInterestRate
    balance -= balance * monthlyPaymentRate
    #print("Month " + str(month) + " Remaining balance: " + str(round(balance, 2)))
    month += 1

print("Remaining balance: " + str(round(balance, 2)))