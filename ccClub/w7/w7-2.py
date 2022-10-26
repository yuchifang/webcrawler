'''
雞胗 雞冠 雞腿 雞屁股
8 12 40 14
48
雞胗 雞腿

肉肉 菜菜 飯飯 菜飯 韓國魚
2 7 11 15 143
9
肉肉 菜菜

'''

inputItem = input().split()
inputPrice = [int(item) for item in input().split()]
input3 = int(input())
newList = []
totalLength = len(inputItem)
dic = {}
buyThing=[]

for index in range(totalLength):
    dic[inputPrice[index]] = index
    if input3-inputPrice[index] in dic:
        buyThing=sorted([index,dic[input3-inputPrice[index]]])
        buyThing =[ inputItem[item] for item in buyThing]

print(" ".join(buyThing))

