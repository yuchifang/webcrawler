import pandas as pd
from sklearn import preprocessing 
labelencoder = preprocessing.LabelEncoder()
people=['kid','youth','old','youth','youth','kid']
age=[5,30,45,35,22,6]
height=[120,150,159,160,183,152]

dic={'People':people,'Age':age,'height':height}
data=pd.DataFrame(dic,columns=["People"])
print(data)
'''
  People  Age  height
0    kid    5     120
1  youth   30     150
2    old   45     159
3  youth   35     160
4  youth   22     183
5    kid    6     152
'''
