'''
1 2 3 4 5 6 7 8 
"8"
1 2 3 5 6 7 8 
"4"
計算連續幾次

1 2 5 6 9
3
'''
# 找到所有值的差 
# 比較哪個最多
count = 0
countList = []
data = [int(item) for item in input().split()]
dataLength = len(data)
dicNumber={}
for index in range(dataLength):
    for index2 in range(index+1,dataLength):
        dicNumber[data[index2]-data[index]]=data[index2]-data[index]
for 
print(dicNumber)