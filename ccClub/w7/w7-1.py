'''
1 2 3 4 5 6 7 8 
"8"
1 2 3 5 6 7 8 
"4"
計算連續幾次

1 2 5 6 9
3
'''
# data = [int(item) for item in input().split()]
# for item in data:
#     # 用物件記錄 key 為差值 value 為陣列
#     pass


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

'''
給定 k 個數(k >= 1)，找出這 k 個數中連續的數（遞增）最多幾次。
Input
輸入為一行，包含數個整數，以空白為間隔
Output
輸出為一行，包含一個數字


0 
0


-5 -4 -3 -2 -1
5


-1 0 1 2 3 4
6




1 2 3 4 5 6 7 8
8 


1 2 3 5 6 7 8
4


取絕對值 的差
'''

input1 = [int(item) for item in input().split()]
totalCountList = []


indexIncrease = 0

'''
1 2 3 5 6 7 8
4
'''
for index,item in enumerate(input1):
    count = 2
    diff = abs(input1[indexIncrease+1]-input1[indexIncrease])
    indexIncrease = indexIncrease+1
    print("indexIncrease",indexIncrease)
    while indexIncrease +1 < len(input1) -1  and input1[indexIncrease] + diff == input1[indexIncrease+1] :
        print(indexIncrease)
        indexIncrease+=1
        count +=1

    totalCountList.append(count)
    if indexIncrease +1 >= len(input1) -1:
        break
print(totalCountList)







    


# print(totalCountList)