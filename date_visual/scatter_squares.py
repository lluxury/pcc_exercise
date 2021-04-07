import matplotlib.pyplot as plt

x_value = list(range(1,1001))
y_values = [x**2 for x in x_value]
# plt.scatter(x_value, y_values,c='red',edgecolors='none', s=40)
# plt.scatter(x_value, y_values,c=(0,0,0.8),edgecolors='none', s=40)
# 自定义
plt.scatter(x_value, y_values,c=y_values,cmap=plt.cm.Blues,edgecolors='none', s=40)
# 渐变

plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

plt.tick_params(axis="both", which='major', labelsize=14)
plt.axis([0,1100,0,1100000])
# plt.show()
plt.savefig('squares_plot.png', bbox_inches='tight')