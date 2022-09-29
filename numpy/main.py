# [20,22,21,19,5,18,20,22,17,19,23,23,22,17,19,20,19,22,18,23]
# 四分位距算法
# import numpy as np
# nums = [20,22,21,19,5,18,20,22,17,19,23,23,22,17,19,20,19,22,18,23]
# data = np.percentile(nums,(25,50,75),method=('midpoint'))
# print("data",data)

# 用 numpy 計算標準差
# ddof=0，回傳 population standard deviation 母體標準差
# ，分母(n)，有偏估計

# ddof=1，回傳 sample standard deviation 樣本標準差
# ，分母(n-1)，無偏估計
import numpy as np
arr = np.array([5,6,8,9])
print(np.std(arr,ddof=1))
# 樣本去估計整體實際的標準差，就應該使用 ddof=1。

# 變異數 
nums = [5,6,8,9]
data = np.var(nums,ddof=1)
print("data",data)