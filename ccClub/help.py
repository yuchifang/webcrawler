'''
Input
共兩行，

第一行包含一正整數 N，為調色盤的格數

第二行包含ㄧ字串，為小仔畫畫使用顏色的順序（以一個字元代表一種顏色）


Output
共一行，包含一整數為小仔在過程中總共洗過幾次調色盤
'''

'''
3
awewaaj
1
'''

'''
4
aedrhews
3

最小洗調色盤次數
'''
input1 = int(input()) 
input2 = list(input())
dictColor = {}
allColor = len(input2)
addColorCount=0
changeColorCount=0

for item in range(allColor):

    if item not in dictColor:
        dictColor[item] = 1
        addColorCount +=1

    if item not in dictColor and addColorCount>=input1:
        changeColorCount +=1

    if item in dictColor:
        pass
    
    
    