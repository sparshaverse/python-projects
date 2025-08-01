import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()
X = np.linspace(0, 2*np.pi, 200)
line1, = ax.plot(X, np.sin(X), label = 'Sine')
line2, = ax.plot(X, np.cos(X), label = 'Cosine')

def animate(i):
    line1.set_ydata(np.sin(X+i/10))
    line2.set_ydata(np.cos(X+i/10))
    return line1, line2


ax.legend()
ani = animation.FuncAnimation(fig, animate, interval=50)
plt.show()