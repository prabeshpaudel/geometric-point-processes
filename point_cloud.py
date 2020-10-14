import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

# uniform
x = np.random.uniform(-10000,10000,1000)
y = np.random.uniform(-10000,10000,1000)
plt.scatter(x,y,s=10)
plt.show()

# normal
x = np.random.normal(0,3000,1000)
y = np.random.normal(0,3000,1000)
plt.scatter(x,y,s=10)
plt.show()

# circular uniform
radius = 10000
a = np.random.uniform(0,1,1000) * 2 * math.pi
r = radius * np.sqrt(np.random.uniform(0,1,1000))
x = r * np.cos(a)
y = r * np.sin(a)
plt.scatter(x,y,s=10)
plt.show()

# circular
radius = 10000
jitter = 1000
a = np.random.uniform(0,1,1000) * 2 * math.pi
r = np.random.normal(radius,jitter,1000)
x = r * np.cos(a)
y = r * np.sin(a)
plt.scatter(x,y,s=10)
plt.show()

# radiating lines
radius = 10000
num_lines = 6
a = np.random.randint(num_lines,size=1000) / num_lines * 2 * math.pi
r = np.random.uniform(0,radius,1000)
x = r * np.cos(a)
y = r * np.sin(a)
plt.scatter(x,y,s=10)
plt.show()