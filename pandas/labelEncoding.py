import numpy as np
import pandas as pd
from sklearn import preprocessing 
labelencoder = preprocessing.LabelEncoder()
people=['kid','youth','old','youth','youth','l']
age=[5,30,45,35,22,6]
height=[120,150,159,160,183,152]

dic={'People':people,'Age':age,'height':height}
data=pd.DataFrame(dic)
print(data)
'''
     Country  Age  Salary
0     Taiwan   25   20000
1  Australia   30   32000
2    Ireland   45   59000
3  Australia   35   60000
4    Ireland   22   43000
5     Taiwan   36   52000
'''
data["Country"] = labelencoder.fit_transform(data["Country"])

print(data)
'''
   Country  Age  Salary
0        2   25   20000
1        0   30   32000
2        1   45   59000
3        0   35   60000
4        1   22   43000
5        2   36   52000
'''