'''
Next steps:
Create graph to visualize.
'''

'''
Goal of project is to track how my high yields savings account performs.
I like to physically see how much money I am earning in interest.
My financial goal for 2026 is to save up 15k. Currently I'm at 6k.
If I can comfortably save 300 per month, how much would I have by the end of one year?
In addition, how long would it take to save up to my goal?
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# parameters
annual_rate = 0.0365
starting_balance = 6000
goal = 15000
# convert annual rate to monthly rate. 
monthly_rate = (1 + annual_rate) ** (1/12) - 1 #equation found on google
monthly_contribution = 300
n = 12

# create schedule
schedule = []
balance = starting_balance

for i in range(1, n + 1):
    balance *= (1 + monthly_rate)
    balance += monthly_contribution
    schedule.append({
        "Month": i,
        "Contribution": monthly_contribution,
        "Interest Rate": round(monthly_rate * 100, 5),
        #"Accumulated": round(accumulated, 2),
        "End Balance": round(balance, 2)
    })

# display the schedule
df_schedule = pd.DataFrame(schedule)
print("*" * 20 + " Initial Table " + "*" * 20)
print(df_schedule)

# insert a row at the very beginning showing what I initially started with
initial = pd.DataFrame({"Month": 0,
                        "Contribution": 0,
                        "Interest Rate": round(monthly_rate * 100, 5),
                        "End Balance": 6000.00},
                        index = [0])
df_schedule = pd.concat([initial, df_schedule]).reset_index(drop = True)

print("*" * 20 + " Starting Balance Table " + "*" * 20)
print(df_schedule)

'''
Note: 
Probably doing this the long way... but now that I have the initial balance as the first row,
I can do column math to find the accumulated :)
'''
df_schedule['Accumulated'] = (df_schedule['End Balance'] - df_schedule['End Balance'].shift(1)) - monthly_contribution

print("*" * 20 + "  Accumulated Table " + "*" * 20)
print(df_schedule)

# How long wil it take to hit my goal?
G = 15000
P = 6000
C = 300
r = 0.0365
n = 12

balance = P
months = 0
monthly_rate = r/n

while balance < G:
    balance = balance * (1 + monthly_rate) + C
    months += 1
print()
print("It will take " + str(months) + " to hit your goal if you save $3oo per month")
print()

# give new parameters with 28 months
# parameters
annual_rate = 0.0365
starting_balance = 6000
goal = 15000
# convert annual rate to monthly rate. 
monthly_rate = (1 + annual_rate) ** (1/12) - 1 #equation found on google
monthly_contribution = 300
n = 28

# create schedule
new_schedule = []
balance = starting_balance

for i in range(1, n + 1):
    balance *= (1 + monthly_rate)
    balance += monthly_contribution
    new_schedule.append({
        "Month": i,
        "Contribution": monthly_contribution,
        "Interest Rate": round(monthly_rate * 100, 5),
        "End Balance": round(balance, 2)
    })
df_goal = pd.DataFrame(new_schedule)

# add initial
initial = pd.DataFrame({"Month": 0,
                        "Contribution": 0,
                        "Interest Rate": round(monthly_rate * 100, 5),
                        "End Balance": 6000.00},
                        index = [0])
df_goal = pd.concat([initial, df_goal]).reset_index(drop = True)

# add accumulated column
df_goal['Accumulated'] = (df_goal['End Balance'] - df_goal['End Balance'].shift(1)) - monthly_contribution

print("*" * 20 + "  28 Month Table " + "*" * 20)
print(df_goal)

# Next steps: How much would I have to save to hit my goal by 2026?