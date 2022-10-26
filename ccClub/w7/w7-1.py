'''
1 2 3 4 5 6 7 8 
"8"
1 2 3 5 6 7 8 
"4"
計算連續幾次

1 2 5 6 9
3
'''
data = [int(item) for item in input().split()]
for item in data:
    # 用物件記錄 key 為差值 value 為陣列
    pass


# todo 解法一
'''
count = 1
countList = []
data = [int(item) for item in input().split()]
dataLength = len(data)
dicDiff={}
dicNumber={}
for index in range(dataLength):
    dicNumber[data[index]]=data[index]
    for index2 in range(index+1,dataLength):
        dicDiff[data[index2]-data[index]]=data[index2]-data[index]
for item in dicDiff:
    for itemNumber in dicNumber:
        key = itemNumber +item
        while key in dicNumber:
            key+=item
            count+=1
            countList.append(count)
        count =1

print(max(countList))
'''