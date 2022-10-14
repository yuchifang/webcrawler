def isAlphabet(item):
    if 65<=ord(item)<=90 or 97<=ord(item)<=122:
        return True
    else:
        return False

def isValid(item):
    if item <91:
        return item+32
    return item

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

newAlphabetDict={}
print(alphabetDict)

for item in alphabetDict:
    if item+32 < 122 and item+32 in alphabetDict:
        newAlphabetDict[item+32] = alphabetDict[item] + alphabetDict[item+32]
    else:
        if item in newAlphabetDict:
            newAlphabetDict[item] =alphabetDict[item]+ newAlphabetDict[item]
        else: # test APPLEappleD and appleAPPLED
            newAlphabetDict[item] =alphabetDict[item]

print(newAlphabetDict)
for item in sorted(newAlphabetDict,key=isValid):
    print(f"{chr(item)}{newAlphabetDict[item]}",end=" ")
