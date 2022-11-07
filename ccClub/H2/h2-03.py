'''
說明：
以範例一為例子。對凱文來說，小明跟他的相似度是 3/4 = 75% >= 50%，小美是 0/4 = 0% < 50%，小華是 2/4 = 50% >= 50%。
因此，我們推薦凱文小明買過但他沒買過的卡片跟機車，還有小華買過但凱文沒買過的番茄。
在輸出的第一行，我們先輸出凱文，接著依照商品出現的順序依序輸出要推薦給凱文的卡片、機車、番茄。

對小明來說，只有凱文跟他的相似度 3/5 = 60% >= 50%，因此我們推薦他凱文買過但他沒買過的鑰匙。
阿小美就是個邊緣人，我們先不理他。

小華跟小明和凱文的相似度是 2/3 = 67% >= 50%，因此我們推薦他凱文跟小明有買但他沒買的錢包、鑰匙、卡片、機車。

輸入為 n + 2 行。
第一行包含一個整數，為判斷相不相似的閾值。
中間 n 行中，每一行包含數個詞，以空白區隔。
最後一行輸入 end，代表輸入結束。


輸出為 n 行，代表對 n 個顧客的推薦商品。

input
50
凱文 電腦 手機 錢包 鑰匙
小明 電腦 手機 錢包 卡片 機車
小美 香蕉 蘿蔔
小華 電腦 手機 番茄
end

output
凱文 卡片 機車 番茄
小明 鑰匙
小美
小華 錢包 鑰匙 卡片 機車


input
50
r S F C D U Q Z
l Q D F S B Z
q Q F U C D
c Z D F U B S Q C
end

output
r B
l C U
q S Z B
c
'''

# 暫定
# input() 百分比
# end 結束
'''
listName = []
dictStaff {
    'r':[item],
    'a':[item2],
    'b':[item3],
    'd':[item4],
}

用 for 回圈 一個迴圈進來 listName = []
for item in listName:
    for key in dicStaff:
        比較目標 Array 和其他的 產生 + 百分比 list 並print
print()
'''

rate = int(input())
dictStaff = {}
go = True
listName = []
while go:
    data = input().split()
    if data[0] == "end":
        go = False
    else:
        listName.append(data[0])

        dictStaff[data[0]] = data[1::]


def getDiffItem(Lst1, Lst2):
    returnList = []
    for item in Lst2:
        if item not in Lst1:
            returnList.append(item)
    return returnList


def getRecommendItem(output_Name):
    global rate
    printList = [output_Name]
    current_List = dictStaff[output_Name]
    current_List_Length = len(current_List)
    repeat_List = []
    for key in dictStaff:
        if key == output_Name:
            continue
        repeat_List = [item for item in dictStaff[key]
                       for target_Item in dictStaff[output_Name] if target_Item == item]
        diff_List = getDiffItem(dictStaff[output_Name], dictStaff[key])
        if (len(repeat_List) / current_List_Length)*100 >= rate:
            printList.extend(diff_List)
    answerList = []
    [answerList.append(item) for item in printList if item not in answerList]
    return answerList


for outputName in listName:
    print(" ".join(getRecommendItem(outputName)))
