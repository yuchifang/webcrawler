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

answer
I have an 「apple」
you are so 「cute」

test case 2
開心 快樂 愉悅
今天的你不得不快樂
快樂且愉悅
end

answer:
今天的你不得不「快樂」
「快樂」且「愉悅」

test case 3
郭婞淳 婞淳 金牌
中華代表團出征東京奧運，目前累積2銀2銅，獨缺金牌還沒拿到，然而今（27日）參加女子59公斤級舉重賽事的「舉重女神」郭婞淳也被看好有望奪金，果然稍早進行的比賽，她以抓舉103公斤、挺舉第一舉125公斤就成功，以總和228公斤海放其他選手，雖然比賽還沒結束，但也確定拿下金牌，同時完成了「金牌大滿貫」，也是本屆奧運中華代表團首面金牌。
今天的比賽，郭婞淳是第9名上場的選手，抓舉開把100公斤輕鬆達成，之後將重量往上加，雖然第二次試舉103公斤遭審判委員挑戰，判定失敗，但第三次試舉維持103公斤成功，抓舉項目擁有7公斤的領先優勢，海放其他選手；到了挺舉開舉，她開把定在全場最高的125公斤也成功舉起，確定拿下金牌。
郭婞淳今天以抓舉103公斤、挺舉133公斤，總和236公斤勝出，三項成績是此次參賽選手之最，也成為最新奧運紀錄保持人。
另外泰國選手蘇甘雅因禁藥問題遭禁賽，郭婞淳實力海放對手，最終順利拿下金牌，完成「金牌大滿貫」。
end

answer
中華代表團出征東京奧運，目前累積2銀2銅，獨缺「金牌」還沒拿到，然而今（27日）參加女子59公斤級舉重賽事的「舉重女神」「郭婞淳」也被看好有望奪金，果然稍早進行的比賽，她以抓舉103公斤、挺舉第一舉125公斤就成功，以總和228公斤海放其他選手，雖然比賽還沒結束，但也確定拿下「金牌」，同時完成了「「金牌」大滿貫」，也是本屆奧運中華代表團首面「金牌」。
今天的比賽，「郭婞淳」是第9名上場的選手，抓舉開把100公斤輕鬆達成，之後將重量往上加，雖然第二次試舉103公斤遭審判委員挑戰，判定失敗，但第三次試舉維持103公斤成功，抓舉項目擁有7公斤的領先優勢，海放其他選手；到了挺舉開舉，她開把定在全場最高的125公斤也成功舉起，確定拿下「金牌」。
「郭婞淳」今天以抓舉103公斤、挺舉133公斤，總和236公斤勝出，三項成績是此次參賽選手之最，也成為最新奧運紀錄保持人。
另外泰國選手蘇甘雅因禁藥問題遭禁賽，「郭婞淳」實力海放對手，最終順利拿下「金牌」，完成「「金牌」大滿貫」。

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
dataItem = {}
for item in input1:
    data = "".join([f"*{str(ord(item)+30000)}" for item in list(item)])
    dictItem[item] = "「" + data + "」"
    dataItem[data] = data

sortedInput1 = sorted(input1, key=len, reverse=True)


isValid = True
while isValid:
    data = input()
    if data == "end":
        isValid = False
    else:
        newData = data
        for item in sortedInput1:
            newData = newData.replace(item, dictItem[item])
        keyStrList = []
        for item in dataItem:
            keyStrList.extend(item.split("*")[1:])
        for item in keyStrList:
            newData = newData.replace(item, chr(int(item)-30000))
        newData = newData.replace("*", "")

        print(newData)
