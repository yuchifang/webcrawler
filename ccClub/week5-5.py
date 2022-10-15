# 兩個數字交換
'''
// todo 對 file 做處理
// 213498
// 找到 最大值 優先
// 再來比較 index 越大越好 後

// 找到最小值 index 優先比對 前

// S2
// 找到 陣列前面最小的數值後 = Y
// 在從後面找 比Y 大的值 交換

// 987
// 從後面找到最大值後 Y
// 從前面找比 Y 小的數字 = null return 原本的值
'''

'''
9876 = 9876
3578 = 8573
102030405060708090 = 902030405060708010
991199 = 999191

/找到最大值 取得
'''

# 988588011 test case
input1 = [int(item) for item in input()]
max = 0
maxIndex = -1
for index in range(len(input1)-1, -1, -1):
    if input1[index] > max:
        max = input1[index]
        maxIndex = index

Index = 0
minIndex = -1
for data in input1:
    if max > data and minIndex == -1:
        minIndex = input1.index(data)
    Index += 1

print("maxIndex", maxIndex)
print("minIndex", minIndex)

if maxIndex > minIndex:
    input1[maxIndex] = input1[minIndex]
    input1[minIndex] = max

print("".join([str(item) for item in input1]))
