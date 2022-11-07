'''
1 2 3 4 5 6 7 8
"8"
1 2 3 5 6 7 8
"4"
計算連續幾次

1 2 5 6 9
3
'''
# data = [int(item) for item in input().split()]
# for item in data:
#     # 用物件記錄 key 為差值 value 為陣列
#     pass


# todo 解法一
'''

count = 1
countList = []
data = [int(item) for item in input().split()]
dataLength = len(data)
dicDiff = {}
dicNumber = {}
for index in range(dataLength):
    dicNumber[data[index]] = data[index]
    for index2 in range(index+1, dataLength):
        dicDiff[data[index2]-data[index]] = data[index2]-data[index]
for item in dicDiff:
    for itemNumber in dicNumber:
        key = itemNumber + item
        while key in dicNumber:
            key += item
            count += 1
            countList.append(count)
        count = 1
print(max(countList))
'''

'''
給定 k 個數(k >= 1)，找出這 k 個數中連續的數（遞增）最多幾次。
Input
輸入為一行，包含數個整數，以空白為間隔
Output
輸出為一行，包含一個數字

0 = 0
1 = 1

-5 -4 -3 -2 -1 = 5
-1 0 1 2 3 4 = 6

1 2 3 4 5 6 7 8 = 8 
1 2 3 5 6 7 8 = 4
1 2 3 4 5 1 2 = 5
1 2 1 2 3 4 5 = 5

5 4 3 2 1 = 1
3 2 3 1 = 2


10 20 30 => 3
30 20 10 => 1
1 1 1 1 1 => 1


1 1 1 2 = 1
-1 -1 -1 -1 0 = 1

1 2 2 2 2 = 2
-2 -1 -1 -1 = 2
-3 -2 -2 -2 -2 = 1


輸入 => 輸出
取絕對值 的差
'''

# todo 把這個修好
'''
input_Number_List = [int(item) for item in input().split()]
total_Count_List = []
index_Increase = 0
for index, number in enumerate(input_Number_List):
    # 如果輸入陣列 長度為一
    if len(input_Number_List) == 1:
        total_Count_List = [1]
        break

    # 預設 count 如果 1 2 為 2
    count = 2

    # 計算  index 1 - index 0 的差
    diff = input_Number_List[index_Increase+1] - \
        input_Number_List[index_Increase]
    # 如果差距 < 0 count = 1  # for 5 4 3 2 1
    if diff <= 0:
        count = 1

    # 比較 index 1 index 2 # for 下面 while 用
    index_Increase += 1

    # diff 小於 0 遞減, 判斷 index_Increase 是否超過最大長度, 判斷 index 3 的值 是否等於 index 2 + diff
    while diff > 0 and index_Increase + 1 != len(input_Number_List) and input_Number_List[index_Increase] + diff == input_Number_List[index_Increase+1]:

        index_Increase += 1
        count += 1

    total_Count_List.append(count)
    if index_Increase + 1 >= len(input_Number_List):
        break

print(max(total_Count_List))
'''


'''
0 = 0
1 = 1

-5 -4 -3 -2 -1 = 5
-1 0 1 2 3 4 = 6

1 2 3 4 5 6 7 8 = 8 
1 2 3 5 6 7 8 = 4
1 2 3 4 5 1 2 = 5
1 2 1 2 3 4 5 = 5

5 4 3 2 1 = 1
3 2 3 1 = 2


10 20 30 => 3
30 20 10 => 1
1 1 1 1 1 => 1


1 1 1 2 = 2
-1 -1 -1 -1 0 = 2

1 2 2 2 2 = 2
-2 -1 -1 -1 = 2
-3 -2 -2 -2 -2 = 1

-1 -2 -3 = 1
-1 -1 -3 = 1
'''

input_Number_List = [int(item) for item in input().split()]
compareList = input_Number_List[1::]
diff = 0
count = 0
total_List_count = []

if len(input_Number_List) == 1:
    total_List_count = [1]

for item1, item2 in zip(input_Number_List, compareList):

    # 初始值
    if count == 0:
        diff = item1 - item2
        if diff < 0:
            count = 2
    else:
        if item1 - item2 == diff:
            count += 1
        else:
            total_List_count.append(count)
            diff = item1 - item2
            if diff < 0:
                count = 2

    if diff >= 0:
        count = 1
    total_List_count.append(count)

print(max(total_List_count))
