'''
想請問一下這一題
[8-綜合] 數列三胞胎
https://judge.ccclub.io/contest/112/problem/22Fall08

對題目的理解是
如果數列中 前兩項的和 等於 後面某一項 
則算成功一次
1 2 3 6
1+2=3 總數+1
共1組

1 3 4 8 2 6
1+3=4 總數+1
4+2=6 總數+1
共2組

1 3 4 8 2 6 10
1+3=4 總數+1
4+2=6 總數+1
8+2=10 總數+1
4+6=10 總數+1
共4組

0 4 4
0+4=4 總數+1
共1組

想請問一下 有什麼解法嗎
'''
data = [int(item) for item in input().split(" ")]
# n=0
# for i in range(2,len(data)):     
#     for j in range(i-1):
#         for k in range(j+1,i):
#             if(data[i] ==data[k]+data[j]):
#                 n+=1
# print(n)

def isValid(dataList):

    totalCount = 0
    for currentNumber in dataList:
        cache = {}
        for index in range(0, dataList.index(currentNumber)+1):
            dataItem = dataList[index]
            # 將值 以key記錄在 cache 中 
            # 出現一次 加1
            if dataItem in cache:
                cache[dataItem] = cache[dataItem]+1
            else:
                cache[dataItem] = 1
            # 如果 currentNumber - dataItem 的值 在cache中
            # 找有沒有對應的key
            if currentNumber - dataItem in cache:
                # 有的話 判斷 相減的值 會不會剛好等於 出現過的值
                # 處理 1 2 4 8 的情況 如果是則跳過
                if dataItem == currentNumber - dataItem and cache[dataItem] == 1:
                    continue
                totalCount += 1


    print(totalCount)


isValid(data)
