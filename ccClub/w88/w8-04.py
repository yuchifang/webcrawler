'''
輸入有 n + 2 行。
第一行是欠債外國人的名字，以空格區隔。
第二行是每個外國人對應的欠款金額，以空格區隔。
最後 n 行中，每行包含一個外國人名字，代表莊主元龍安排的催討順序。

輸出有 n 行，代表小明依序要催討的金額。
Ana Bumper Cindy David
100 200 300 400
Ana
Cindy
Ana
Cindy
Bumper
Ana

100
300
100
300
200
100
'''
dataName = sorted(input().split())
dataCost = [int(item) for item in input().split()]
dataDataList = list(zip(dataName,dataCost))

count = 0
def binarySearch(target,dataDataList):
    global count
    count +=1
    if count ==20:
        return
    print(dataDataList)
    midIndex = len(dataDataList)//2

    if dataDataList[midIndex][0] == target:
        return dataDataList[midIndex][1]
    if dataDataList[midIndex][0] > target:
        return binarySearch(target,dataDataList[0:midIndex:])
    if dataDataList[midIndex][0] < target:
        return binarySearch(target,dataDataList[midIndex::])
    if len(dataDataList) == 1:
        return
print(binarySearch("Ana",dataDataList))
