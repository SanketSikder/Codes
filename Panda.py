import pandas as pd
import matplotlib.pyplot as plt
"""
df = pd.read_csv('C:/Users/Titin/Desktop/Python/nyc-weather.csv')
print(df.head())
print(df["Temperature"].max())
print(df["EST"][df["Events"]=="Rain"])
print(df.fillna(0))
print(df["WindSpeedMPH"].mean())

weather_data=[
 ('1/1/2022',32,6,'Rain'),
 ('1/2/2022',35,7, 'Sunny'),
 ('1/3/2022',2,2, 'Snow' )
]
df=pd.DataFrame(weather_data,columns=["day","Temp","Windspeed","Events"])
print(df)

df=pd.read_csv(r"C:\ Users\Titin\Desktop\Python\weather_by_cities.csv")
#print(df)
g=df.groupby(["city"])
print(g.max())

df1=pd.DataFrame({
    "city":["Washington","Newyork","orlando"],
    "Temperature":[34,25,30]
})
df2=pd.DataFrame({
    'city':['chennai','hyderabad','bangalore'],
    'Temperature':[34,30,29]
})

df=pd.concat([df1,df2],ignore_index=True)
print(df)

df=pd.concat([df1,df2],keys=["us","India"])
print(df)
print(df.loc["India"])
"""

