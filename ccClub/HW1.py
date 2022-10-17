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

for item in alphabetDict:
    # 如果 大寫小寫都存在在 dict 中 則相加
    if item+32 < 122 and item+32 in alphabetDict:
        newAlphabetDict[item+32] = alphabetDict[item] + alphabetDict[item+32]
    else:
        # 處理小寫 or 只有大寫自己的情況
        if item in newAlphabetDict:
            pass
        else: # test APPLEappleD and appleAPPLED
            newAlphabetDict[item] =alphabetDict[item]

for item in sorted(newAlphabetDict,key=isValid):
    if item < 91 :
        print(f"{chr(item+32)}{newAlphabetDict[item]}",end=" ")
    else:
        print(f"{chr(item)}{newAlphabetDict[item]}",end=" ")
