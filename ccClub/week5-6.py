'''
開心 快樂 愉悅
今天的你不得不快樂
快樂且愉悅
end

今天的你不得不「快樂」
「快樂」且「愉悅」

'''
"「"
"」"

'''
test case 1

apple app cute
I have an apple
you are so cute
end

test case 2
開心 快樂 愉悅
今天的你不得不快樂
快樂且愉悅
end



'''
'''
S1
對每一行依據 
替換長度為優先 做替換 
替換完改變字串 在每個字串中 加入*
（判斷 替換字串長度）
S2
轉換為特殊字元 for 題目描述
'''

# 試著單行單行看


input1 = input().split()
dictItem = {}
for item in input1:
    data="*".join(list(item))
    dictItem[item] = "「" + data +"」"

sortedInput1 = sorted(input1,key=len,reverse=True)
print("test")
print(sortedInput1)
print("test")
isValid = True
while isValid:
    data = input()
    print("-----------")
    print(data)
    if data == "end":
        isValid = False
    else:
        newdata = data
        for item in sortedInput1:
            newdata = newdata.replace(item, dictItem[item])
        print(newdata.replace("*",""))