# import pandas as pd
# left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
#                  'key2': ['K0', 'K1', 'K0', 'K1'],
#                  'A': ['A0', 'A1', 'A2', 'A3'],
#                  'B': ['B0', 'B1', 'B2', 'B3']})
# right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
#                       'key2': ['K0', 'K0', 'K0', 'K0'],
#                       'C': ['C0', 'C1', 'C2', 'C3'],
#                       'D': ['D0', 'D1', 'D2', 'D3'],
#                       'E': [1,2,3,4]})


# # data2 = pd.merge(left,right)
# # print(data2)
# # left
# '''
#   key1 key2   A   B
# 0   K0   K0  A0  B0
# 1   K0   K1  A1  B1
# 2   K1   K0  A2  B2
# 3   K2   K1  A3  B3
# '''
# # right
# '''
#   key1 key2   C   D  E
# 0   K0   K0  C0  D0  1
# 1   K1   K0  C1  D1  2
# 2   K1   K0  C2  D2  3
# 3   K2   K0  C3  D3  4
# '''

# data =pd.merge(left, right, right_on=['E'], left_index = True, how = 'outer')
# print(data)

# import pandas as pd
# listOne = range(3)
# listTwo = ["A","B","C"]
# df1 = pd.DataFrame({"data2":listOne,"name":listTwo})
# print(df1)
# listT = range(5,0,-1)
# listF = ["A","B","C","D","C"]
# df2 = pd.DataFrame({"data1":listT,"name":listF})
# print(df2)
# df3 = pd.merge(df1,df2,left_index=True,right_on="data1")
# # df3 = pd.merge(df1,df2,left_on="data2",right_index=True)
# print(df3)

# import pandas as pd
# listOne = range(3)
# listTwo = ["A","B","C"]
# df1 = pd.DataFrame({"data":listOne,"name":listTwo})


# name = ["D"]
# listThree = [5]
# dict2 = {"name": name,
#                       "data": listThree
# }

# # 建立第二個 data frame
# df2 = pd.DataFrame(dict2)
# print(df1)
# print(df1.unstack())
# print(df1.stack())

# concatData = pd.concat([df1,df2])
# print(concatData)

# some = range(4)
# df3 = pd.DataFrame({"age":some})
# print(df3)

# df4 = pd.concat([concatData,df3],axis=0)
# print(df4)
# 分箱
from matplotlib.pyplot import pink
import pandas as pd
import numpy as np
# data1 = [1,2,3,10,12,15]
# name = ["A","B","C","D","E","F"]
# df1 = pd.DataFrame({"name":name,"data1":data1})
# # print(df1)
# df1['data1'] = pd.cut(x=df1['data1'], bins=[0, 10,25 ])
# print(df1['data1'].unique())
# https://www.javatpoint.com/pandas-dataframe-cut#:~:text=Pandas%20DataFrame.-,cut(),variable%20to%20a%20categorical%20variable.

# data = pd.cut(np.array([1, 7, 5, 4, 6, 3]), 3)
# print(data)
# data2 = pd.cut(np.array([1, 7, 5, 4, 6, 3]), 3,
#                labels=["bad", "medium", "good"])
# print(data2)
# 顯示區間
# https://pandas.pydata.org/docs/reference/api/pandas.cut.html?highlight=cut#pandas.cut

info_nums = pd.DataFrame({'num': np.random.randint(1, 50, 11)})
# print(info_nums)
info_nums['num_bins'] = pd.cut(x=info_nums['num'], bins=[
                               1, 25, 50], right=False)
print(info_nums)
print("----------")
print(info_nums['num_bins'])
print("******")
print(info_nums['num_bins'].unique())
