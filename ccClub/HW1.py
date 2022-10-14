def isAlphabet(item):
    if 65<=ord(item)<=90 or 97<=ord(item)<=122:
        return True
    else:
        return False

input1 = list(input())
data=filter(isAlphabet,input1)
alphabetDict={}
for item in data:
    AscItem = ord(item)
    try:
        alphabetDict[AscItem]
    except KeyError:
        alphabetDict[AscItem] = 1
    else:
        alphabetDict[AscItem] = alphabetDict[AscItem] + 1

print(alphabetDict)

for item in alphabetDict:
    print("item",item)
    if item+32 < 122 and item+32 in alphabetDict:
        alphabetDict[item+32] = alphabetDict[item] + alphabetDict[item+32]
        del alphabetDict[item]

print(alphabetDict)
