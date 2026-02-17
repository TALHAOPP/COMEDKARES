import matplotlib.pyplot as plt

plt.subplot(1, 2, 1)
plt.bar(['Electronics', 'Clothing', 'Home'], [300, 450, 200])
plt.title("Sales by Category")

plt.subplot(1, 2, 2)
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 11]
plt.plot(x, y)
plt.title("Trend Line")

plt.tight_layout()
plt.show() 