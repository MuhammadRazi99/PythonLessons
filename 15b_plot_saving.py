import matplotlib.pyplot as plt
x=[0,2,4,6]
y=[1,3,4,8]
plt.plot(x,y)
plt.xlabel("x values")
plt.ylabel("y values")
plt.legend(["data 1"])
plt.title("graph of x and y")

# saving the graph
plt.savefig('15b_plot1.png',dpi=350)
plt.show()