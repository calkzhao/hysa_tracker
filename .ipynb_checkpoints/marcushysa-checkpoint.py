'''
Last edited July 18, 2025
Next steps:
Add column to see how much in interest I am earning.
How long till I can hit my goal?
Create graph to visualize.
'''

'''
Goal of project is to track how my high yields savings account performs.
I like to physically see how much money I am earning in interest.
My financial goal for 2026 is to save up 15k. Currently I'm at 6k.
If I can comfortably save 150 per paycheck, how much would I have by the end of one year?
In addition, how long would it take to save up to my goal?
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# parameters
annual_rate = 0.0365
starting_balance = 6000
goal = 15000
# convert annual rate to biweekly rate. 
biweekly_rate = (1 + annual_rate) ** (1/26) - 1 #equation found on google
biweekly_contribution = 150
# 26 pay periods in a year
n = 26

# create schedule
schedule = []
balance = starting_balance

for i in range(1, n + 1):
    balance *= (1 + biweekly_rate)
    balance += biweekly_contribution
    schedule.append({
        "Biweekly Period": i,
        "Contribution": biweekly_contribution,
        "Interest Rate": round(biweekly_rate * 100, 5),
        #"Accumulated": round(accumulated, 2),
        "End Balance": round(balance, 2)
    })

# display the schedule
df_schedule = pd.DataFrame(schedule)
# print(df_schedule)

# insert a row at the very beginning showing what I initially started with
initial = pd.DataFrame({"Biweekly Period": 0,
                        "Contribution": 0,
                        "Interest Rate": round(biweekly_rate * 100, 5),
                        "End Balance": 6000.00},
                        index = [0])
df_schedule = pd.concat([initial, df_schedule]).reset_index(drop = True)
print("**********FIRST DATAFRAME**********")
print(df_schedule)

'''
Note: 
Probably doing this the long way... but now that I have the initial balance as the first row,
I can do column math to find the accumulated :)
'''
df_schedule['Accumulated'] = (df_schedule['End Balance'] - df_schedule['End Balance'].shift(1)) - biweekly_contribution

print("**********ACCUMULATED DATAFRAME**********")
print(df_schedule)

