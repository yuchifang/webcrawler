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
498712301 = 948712301 
988588011 = 988885011
98769 = 99768
/找到最大值 取得
'''

# 988588011 test case
# 把所有的值 位置都記錄起來
# 第一個數字不能為0

# 想想有沒有更快的解法 一次迴圈?
# Time Limit Exceeded
# todo
# input1 = [int(item) for item in input()]


# totalInputLength = len(input1)
# def isValid(input1):
#     temp = 0
#     indexCount = 0
#     # 從頭開始找值
#     for item in input1:
#         # 從尾開始找值
#         for insideIndexCompare in range(totalInputLength-1, indexCount, -1):
#             input2 = input1.copy()
#             # 如果尾比頭大 交換
#             if input1[insideIndexCompare] > item:
#                 input2[indexCount] = input2[insideIndexCompare]
#                 input2[insideIndexCompare] = item
#                 data = int("".join(input2))
#                 # 紀錄值替換後的值 為了此內層for比大小用
#                 if data > temp:
#                     temp = data
#         if temp != 0:
#             return temp
#         indexCount += 1


# data = isValid(input1)
# if data:
#     print(data)
# else:# 沒找到 print 原字串
#     print("".join(input1))


# # other guy answer
# # [*input()] ??
# lIndex[lIndex],lIndex[RIndex]=input1[RIndex],input1[lIndex]


input1 = [int(x) for x in [*input()]]
tMax = -1
tMaxIndex = -1
lIndex = -1
RIndex = 0

for index in range(len(input1)-1, -1, -1):
    if input1[index] > tMax:  # 從找尾最大值
        tMax = input1[index]
        tMaxIndex = index
        continue
    if input1[index] < tMax:  # 從 比最大值小的值
        lIndex = index
        RIndex = tMaxIndex
if lIndex == -1:
    print(int("".join(map(str, input))))
else:
    input1[lIndex], input1[RIndex] = input1[RIndex], input1[lIndex]
    print(int(''.join(map(str, input1))))

# 用 [8,3,7,6] 做 sorted 與原字串 做比較
# 比與此數列

'''

input1 = [int(item) for item in input()]
maxValue = -1
maxIndex = 0
maxValueMinIndex = -1
minValue = 0
for item in input1:
    if maxValue <= item and maxIndex != 0 and max(input1) > item:
        maxValue = item
        maxValueMinIndex = maxIndex
    maxIndex += 1
for index in range(maxValueMinIndex):
    if input1[index] < maxValue:
        input1[index], input1[maxValueMinIndex] = maxValue, input1[index]
        break
print("".join([str(item) for item in input1]))

9876 = 9876
3578 = 8573
102030405060708090 = 902030405060708010
991199 = 999191
498712301 = 948712301 
988588011 = 988885011
98769 = 99768
997788
'''
