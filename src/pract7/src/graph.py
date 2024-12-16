#!./venv/bin/python3

import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates as mdates
from datetime import datetime

csv_file = "./ganttcl.csv"
df = pd.read_csv(csv_file)
print(df)

df['Start'] = pd.to_datetime(df['Start'])
df['Finish'] = pd.to_datetime(df['Finish'])

fig, ax = plt.subplots(figsize=(10, 6))

for i, task in df.iterrows():
    ax.barh(
        task['Name'], (task['Finish'] - task['Start']).days+1, 
        left=task['Start'], 
        height=0.5
        )

ax.xaxis.set_major_formatter(mdates.DateFormatter('%d.%m.%Y'))
ax.xaxis.set_major_locator(mdates.MonthLocator())
plt.xticks(rotation=45)

ax.set_xlabel('Даты')
ax.set_ylabel('Задачи')
ax.set_title('Диаграмма Ганта')

plt.tight_layout()
plt.show()

