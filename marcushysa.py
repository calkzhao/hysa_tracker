'''
Last edited July 18, 2025
Next steps:
Add column to see how much in interest I am earning.
Create graph to visualize.
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#parameters
annual_rate = 0.0365
starting_balance = 6000
goal = 15000
#convert annual rate to biweekly rate
biweekly_rate = (1 + annual_rate) ** (1/26) - 1
biweekly_contribution = 150
n = 26

#create schedule
schedule = []
balance = starting_balance

for i in range(1, n + 1):
    balance *= (1 + biweekly_rate)
    balance += biweekly_contribution
    schedule.append({
        "Biweekly Period": i,
        "Contribution": biweekly_contribution,
        "Interest Rate": round(biweekly_rate * 100, 5),
        "End Balance": round(balance, 2)
    })

#display the schedule
df_schedule = pd.DataFrame(schedule)
print(df_schedule)

