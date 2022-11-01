'''
1 2 3 4 5 6 7 8
"8"
1 2 3 5 6 7 8
"4"
計算連續幾次

1 2 5 6 9
3
'''
# todo 解法一
'''

count = 1
countList = []
data = [int(item) for item in input().split()]
dataLength = len(data)
dicDiff = {}
dicNumber = {}
for index in range(dataLength):
    dicNumber[data[index]] = data[index]
    for index2 in range(index+1, dataLength):
        dicDiff[data[index2]-data[index]] = data[index2]-data[index]
for item in dicDiff:
    for itemNumber in dicNumber:
        key = itemNumber + item
        while key in dicNumber:
            key += item
            count += 1
            countList.append(count)
        count = 1
print(max(countList))
'''
# 0 = 0
# 1 2 3 4 5 6 7 8 = 8
# 1 2 3 5 6 7 8 = 4
# 1 2 5 6 9 = 2

data = [int(item) for item in input().split()]


def isValid(data):
    diff = 0
    count = 1
    countList = []
    dataLength = len(data)
    for index, item in enumerate(data):  # enumerate
        if len(data) == 1:
            return [0]
        if index+1 == dataLength:
            if data[index] - data[index-1] == diff:
                count += 1
                countList.append(count)
            else:
                count = 1
                countList.append(count)

            break

        if diff != item - data[index+1]:
            countList.append(count)
            count = 2
            diff = item - data[index+1]
        elif diff == item - data[index+1]:
            count += 1
    return countList


print(max(isValid(data)))
