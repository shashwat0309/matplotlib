import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0,7])
ypoints = np.array([0,250])
zpoints = np.array([50,350])
wpoints = np.array([0,8])
plt.plot(xpoints,ypoints,wpoints,zpoints)
plt.show()