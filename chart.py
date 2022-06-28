import matplotlib.pyplot as plt
"""
#Line Plot
x=[1,2,3,4,5,6]
y=[50,45,30,35,40,50]
plt.xlabel('Day')
plt.ylabel("Temp")
plt.title("Weather")
plt.plot(x,y,color="green",marker="x",linestyle="dotted")
plt.show()

#Scatter Plot
x=[1,2,3,4,5,6]
y=[50,45,30,35,40,50]
plt.xlabel('Day')
plt.ylabel("Temp")
plt.scatter(x,y)
plt.show()

days = [1,2,3,4,5,6,7]
max_t = [50,51,52,48,47,49,46]
min_t = [43,42,40,44,33,35,37]
avg_t = [45,48,48,46,40,42,41]
plt.plot(days, max_t, label ='max')
plt.plot(days, avg_t, label ='avg')
plt.plot(days, min_t, label ='min')
plt.legend(loc="best")
plt.show()

#bar Graph
company = ['GOOGL', 'AMZN', 'MSFT','FB']
revenue = [90, 136, 80, 27]
plt.xlabel=("Tech Gaints")
plt.ylabel=("Revenue")
plt.bar(company,revenue,label="Revenue")
plt.show()
"""
#pie Chart
x = [10000, 6500, 1500, 3000, 4000]
y = ['Home Rent','Food','Phone/Internet Bill', 'Car Repairs','Other expenses']
plt.pie(x, labels=y,autopct="%1.2f%%")
plt.show()




