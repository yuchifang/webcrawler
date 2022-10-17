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
input1 = input().split()
dictItem = {}
for item in input1:
    dictItem[item] = "「" + item+"」"

data = ""
while data != "end":
    data = input()
    for item in dictItem:
        print(data.replace(item, dictItem[item]))
