import pandas as pd
import calendar

triple_witching = []
options_expiration = []

# options expire 3rd Friday of every month
# triple witching is the last options expiration of each quarter
for i in range(2000, 2025):
    caly = calendar.Calendar().yeardatescalendar(i, 1)
    for x in range(12):
        if x in [2, 5, 8, 11]:
            triple_witching.append(str(caly[x][0][2][4]))
            options_expiration.append(str(caly[x][0][2][4]))
        else:
            options_expiration.append(str(caly[x][0][2][4]))

# get trading days from stock historical data
data = pd.read_csv("SPY_daily.csv", index_col=0, header=0)

cal = data[['date']]

cal['options expiration'] = cal['date'].apply(lambda x: 1 if x in options_expiration else 0)
cal['triple witching'] = cal['date'].apply(lambda x: 1 if x in triple_witching else 0)
    
print(cal)
cal.to_csv("market_calendar.csv")
