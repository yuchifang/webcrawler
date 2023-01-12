from email.policy import default
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# n = 10000
df = pd.DataFrame({'x':[1,2,3,4,5,9,10,11],
                   'y': [1,2,3,4,5,6,7,8],
                   'c':[2,4,6,8,10,12,14,16]
                   },)
ax = df.plot.hexbin(x='x', y='y', gridsize=10,figsize=(4,4),C='c',reduce_C_function=np.amin)
plt.show()