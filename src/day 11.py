
import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [2,4,6,8,11]
plt.plot(x,y)
plt.show()

# SCATTER
x = [1,2,3,4,5]
y = [5,4,3,2,1]

plt.scatter(x,y)
plt.show()

# BAR CHART

catagories = ['TALHA','UMAR','AMAAN','OMER','MAAZ']
values = [30,10,20,50,20]
plt.bar(catagories,values)
plt.show()


plt.subplot(2 , 3 , 5)
#(row , column , position)
plt.plot([1,2,3],[1,4,9])
plt.title("Line Plot")
plt.subplot(1,2,2)
plt.bar(['A','B','C'],[3,7,5])
plt.title("Bar Chart")
plt.show()

#TASK 1
import matplotlib.pyplot as plt
months = [1, 2, 3, 4, 5]
revenue = [2000, 4500, 4000, 7500, 9000]
plt.plot(months,revenue)
plt.title("Monthly Revenue Growth")
plt.xlabel("Months")
plt.ylabel("Revenue in USD")
plt.show()













