#%%
import numpy as np
import matplotlib.pyplot as plt

x= np.arange(0,100)
y= np.sin(x)

plt.plot(x,y)
plt.show()
plt.plot(x,y**2)

#%%

plt.plot(x,y**3)