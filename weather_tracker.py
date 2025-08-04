import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("weather/weather.csv")
print(df.head())
maxTemp=df['MaxTemp']
# plt.plot(df.index,maxTemp,label='MaxTemp')
# plt.title('Temperature trends')
# plt.ylabel('MaxTemp')
# plt.xlabel('Observation Number')
# plt.legend()


#rain
# # Create a new column representing 30-day intervals
df['Interval'] = (df.index // 30) + 1   # Interval 1, 2, 3, ...

# Group rainfall by these intervals ( mean)
# rainfall_30d = df.groupby('Interval')['Rainfall'].mean()
# plt.bar(rainfall_30d.index,rainfall_30d,color='yellow',label='Rainfall')
# plt.title('Rainfall trends')
# plt.xlabel('montly rain')
# plt.ylabel('mean of montly rain data')
# plt.legend()


# humidity
plt.hist(df['Humidity9am'],bins=30,edgecolor='black',label='humidity')
plt.xlabel('Humidity')
plt.ylabel('30 days interval')
plt.legend()
plt.title('Humidity')
plt.show()