import numpy as np
import matplotlib.pyplot as plt
x=np.arange(0,4*np.pi,0.1)
y=np.sin(x)
z=np.cos(x)

fig, ax = plt.subplots()

ax.plot(x,y)
ax.plot(x,z)

ax.set_title("two trignometeric func")
ax.legend(['sin','cos'])
ax.xaxis.set_label_text('Angle')  
ax.yaxis.set_label_text('Sine and Cosine')

plt.show()