# 兩個數字交換
'''
9876 = 9876
3578 = 8573
102030405060708090 = 902030405060708010
991199 = 999191

/找到最大值 取得
'''




input1=[int(item) for item in input()]
max = 0
maxIndex = -1
for index in range(len(input1)-1,-1,-1):
    if input1[index] > max:
        max =  input1[index]
        maxIndex = index

Index = 0
minIndex = -1
for data in input1:
    if max > data and minIndex ==-1:
        minIndex = input1.index(data)
    Index+=1

if maxIndex > minIndex:
    input1[maxIndex] =input1[minIndex]
    input1[minIndex] = max

print("".join([str(item) for item in input1]))