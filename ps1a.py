import numpy as np

# inputs
total_cost = 1000000
portion_down_payment = 0.25
current_savings = 0
r = 0.04
annual_salary = 120000
portion_saved = 0.10

# set counters
required = total_cost * portion_down_payment
month_count = 0

# calculate months
while current_savings < required:

    # set modifiers
    monthly_conts = (annual_salary * portion_saved) / 12
    monthly_int = (current_savings * r) / 12
    
    # increase current savings
    current_savings += monthly_conts + monthly_int
        
    # increase counter
    month_count += 1

# print months to down payment 
print("Target: ",required)
print("Number of months:",month_count) # 183