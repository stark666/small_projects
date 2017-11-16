import numpy as np
import matplotlib.pyplot as plt

def f1(t):
    return np.exp(-t)*np.cos(2*np.pi*t)

def f2(t):
    return np.sin(2*np.pi*t)*np.cos(3*np.pi*t)

def f3(x):
	return np.sqrt(100+np.square(x))+np.sqrt(100+np.square(25-x))/2
# t = np.arange(0.0,5.0,0.02)

t = np.arange(0.0,25.0,0.1)


plt.figure()
plt.plot(t,f3(t),"g-",label="$f(t)=e^{-t} \cdot \cos (2 \pi t)$")
# plt.plot(t,f1(t),"g-",label="$f(t)=e^{-t} \cdot \cos (2 \pi t)$")
# plt.plot(t,f2(t),"r-.",label="$g(t)=\sin (2 \pi t) \cos (3 \pi t)$",linewidth=2)

plt.axis([0.0,12.01,20.0,24.5])
plt.xlabel("t")
plt.ylabel("v")
plt.title("a simple example")

plt.grid(True)
plt.legend()
plt.show()