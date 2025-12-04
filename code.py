import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')
df.columns = df.columns.str.lower()

hot_day = df['temp'].max()
cold_day = df['temp'].min()
avg_temp = df['temp'].mean()
rainfall_total = df['rainfall'].sum()
hot_day_num = df['temp'].idxmax() + 1
cold_day_num = df['temp'].idxmin() + 1


print("The hottest day recorded a temperature of:", hot_day, "°C", " on day", hot_day_num , 'day')
print("The coldest day recorded a temperature of:", cold_day, "°C", " on day", cold_day_num , 'day')
print("The average temperature is:", round(avg_temp, 2) , "°C")
print("The total rainfall throughout the days is:", rainfall_total , "mm")


plt.figure(figsize=(10,5))
plt.plot(df['day'], df['temp'], marker='o', label='Temperature (°C)', color='red')
plt.xlabel('Day')
plt.ylabel('Temperature (°C)')
plt.title('Temperature Data')
plt.legend()
plt.show()

plt.figure(figsize=(10,5))
plt.bar(df['day'], df['rainfall'], color='blue', alpha=0.7, label='Rainfall (mm)')
plt.xlabel('Day')
plt.ylabel('Rainfall (mm)')
plt.title('Rainfall Data')
plt.legend()
plt.show()



