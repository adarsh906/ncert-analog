import numpy as np
import matplotlib.pyplot as plt

def cos(t):
    return a * np.cos(2 * np.pi * f * t)
a = 240 * np.sqrt(2)
f = 50

d = 0.04
t = np.linspace(0 , d , int(1e5))

plt.figure()
plt.plot(t,cos(t))
plt.xlabel('Time')
plt.ylabel('Voltage')
plt.title('Plot of V')
plt.grid(True)
plt.show()
