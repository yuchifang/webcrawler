data = int(input())
data2 = sorted([int(item) for item in input().split()])
dictObj = {}
answer = False
for item in range(data2[0], data2[1]+1):
    key1 = data**2-item**2
    dictObj[item**2] = 1
    if key1 in dictObj:
        answer = True
        break
    else:
        dictObj[key1] = 1
print(answer)
