input1 = int(input())
dataList = []
for row in range(input1):
    lst = input()
    dataList.append([int(item) for item in lst.split(",")])
data = list(map(list, zip(*dataList)))
data1 = list(map(lambda a: a[::-1], data))
for row in data1:
    print(",".join([str(item) for item in row]))
