import numpy as np
import pandas as pd
people=['kid','youth','old','youth','youth','kid']
age=[5,30,45,35,22,6]
height=[120,150,159,160,183,152]
country = ["US","UK","JP","US","UK","JP"]
dic={'People':people,'Age':age,'height':height,"country":country}
data=pd.DataFrame(dic)
data_dum = pd.get_dummies(data.country,prefix='country')
ans = data.join(data_dum)
print(ans)