'''

舉例來說：玩家可以消費 350 金幣購買一個把長劍，消費 450 金幣購買一個抗魔斗篷，並且額外花費 600 金幣將兩者合成為吸魔劍，總共花費 1400 金幣。

輸入的第一部分為取得公式，其中第一行n為取得公式的數量，以下為n行取得公式。
[裝備] [金額] [所需裝備1] [所需裝備2]
若該道具可以直接購買，則所需裝備的位置會留空

輸入的第二部分為想取得的道具，其中第一行 m 為想取得的道具數量，以下 m 行各包含一個字串為道具名稱。
道具的取得之間是獨立的，每一次所要花費的金幣並不會因為你上一次取得了這次所需的道具而改變。
輸出包含m行，每行為各個想購買的道具的總價。


輸入的第一部分為 n+1 行，其中第一行 n 為取得公式的數量，以下為 n 行取得公式。
取得裝備的公式格式如下：[裝備] [金額] [所需裝備1] [所需裝備2]...

輸入的第二部分為 m+1 行，其中第一行 m 為想取得的道具數量，
以下 m 行各包含一個字串為道具名稱。
輸出包含m行，每行為各個想購買的道具的總價。

3
長劍 350
抗魔斗篷 450
吸魔劍 600 長劍 抗魔斗篷
2
長劍
吸魔劍

350
1400



2
a 100 b b b
b 1
2
a
b

103
1
'''
# 可能有三層的結果
'''

5
c 100 a b
a 200 d e
b 300 d d
d 10
e 20


2
a 100 b b b
b 1
2
a
b



a = b + c
c = d + d
b = e + e

a + c + d (?


5
a 100 b b b c
b 1 d d
c 2 e e
d 3
e 3
2
a
b
129
7
'''

menuCost = {}
menuItem = {}
input1 = int(input())
for item in range(input1):
    inputList = input().split()
    menuCost[inputList[0]] = int(inputList[1])
    menuItem[inputList[0]] = inputList[2::]

input2 = int(input())


def handleCost(wantItem: str):
    subTotal = [handleCost(item) for item in menuItem[wantItem]]
    return menuCost[wantItem] + sum(subTotal)


for item in range(input2):
    data = input()
    print(handleCost(data))

# 方法二

menuCost = {}
menuItem = {}
input1 = int(input())
for item in range(input1):
    data = input().split()
    menuCost[data[0]] = int(data[1])
    if len(data) < 3:
        continue
    menuItem[data[0]] = data[2::]


totalWantItem = []


def handleCost(wantItem: str):
    data = []
    if wantItem in menuItem:
        data = [handleCost(data) for data in menuItem[wantItem]]
    return menuCost[wantItem] + sum(data)


input2 = int(input())
for item in range(input2):
    data = input()
    newCount = handleCost(data)
    print(newCount)
