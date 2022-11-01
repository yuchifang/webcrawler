'''
mainClassDict

紀錄 wantItem

輸入為五行。
前四行每一行的第一個名詞是該課的課名，空格以後是修習該課需要的先備知識。
最後一行則是學弟妹好奇的課。

最後一行 有可能有多個
'''
mainClassDict = {}
for item in range(4):
    data = input().split()
    if len(data) > 1:
        mainClassDict[data[0]] = data[1::]
    else:
        mainClassDict[data[0]] = data[0]

wantItem = input()

print(mainClassDict)

count = 0


def getAllClass(inputItem, count):
    print(count)
    count += 1
    if count > 20:
        return
    if inputItem in mainClassDict and type(mainClassDict[inputItem]) == list:
        return [getAllClass(item, count) for item in mainClassDict[inputItem]]
    else:
        return inputItem


print(getAllClass(wantItem, count))
