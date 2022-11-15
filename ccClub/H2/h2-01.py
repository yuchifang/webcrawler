'''
mainClassDict

紀錄 wantItem

輸入為五行。
前四行每一行的第一個名詞是該課的課名，空格以後是修習該課需要的先備知識。
最後一行則是學弟妹好奇的課。

最後一行 有可能有多個 **

a b c
b e
c d
f
a

d e b c a


DataScience calculas stats
calculas counting
stats
counting
DataScience

counting calculas stats DataScience
'''
mainClassDict = {}
for item in range(4):
    data = input().split()
    if len(data) > 1:
        mainClassDict[data[0]] = data[1::]
wantItem = input()

print(mainClassDict)

count = 0

returnList = [wantItem]
returnListLength = len(returnList)
# phaseList = []

'''
DataScience calculas stats
calculas counting
stats
counting
DataScience

'''

'''
a b c
b e
c d
f
a

d e b c a
'''

phaseList = []
def getAllClass(inputItem):
    global returnList, count, phaseList

    if count > 20:
        return
    # if inputItem in mainClassDict and len(mainClassDict[inputItem]) > 1:
    if inputItem in mainClassDict:
        returnList = phaseList + returnList
        phaseList = []
        for item in mainClassDict[inputItem]:
            print("item", item)
            phaseList.append(item)

        for item in mainClassDict[inputItem]:
            getAllClass(item, phaseList)

        



getAllClass(wantItem)
print(" ".join(returnList))

'''
a b c
b e
c d q
f
a
d e b c a
'''

# 不太知道同層 怎麼處理子層 順序的比較
