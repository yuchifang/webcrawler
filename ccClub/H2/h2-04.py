'''
4 3 2 1
b b a c

2 4 1 3

----------------

1 2 3 4 5 6
c c c l u b

6 1 4 5 2 3


看看這個code 依據題目要求結果如何
6 4 3 2 1 7
c c c l u b
'''

input1Number = [int(item) for item in input().split()]
input2Level = [item for item in input().split()]
dic={}
totalLength = len(input2Level)

for index,item in enumerate(input1Number):
    level = input2Level[index]
    if level in dic:
        dic[level].append(item)
    else:
        dic[level] =[item]

returnArr =[]
sortedDic = sorted(dic)
outSideCount =0
while outSideCount<totalLength:
    def appendFun(count):
        newCount = count
        for item in sortedDic:
            if item in dic and len(dic[item])>0:
                returnArr.append(str(dic[item].pop(0)))
                newCount += 1
        return newCount

    if outSideCount<totalLength:
       outSideCount = appendFun(outSideCount)
print(" ".join(returnArr))
