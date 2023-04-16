import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# 載入繪製相關圖的模組 import the Autocorrelation Plot module
from pandas.plotting import autocorrelation_plot

spacing = np.linspace(-9 * np.pi, 9 * np.pi, num=1000)
data = pd.Series(0.7 * np.random.rand(1000) + 0.3 * np.sin(spacing))
print(spacing)
autocorrelation_plot(spacing)
plt.show()
