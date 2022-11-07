input1 = [float(item) for item in input().split(",")]
max_Index, min_Index = len(input1)-1, 0
right_Total = 0
left_Total = 0

left_Temp = 0
right_Temp = 0

right_Total += input1[max_Index]
left_Total += input1[min_Index]

while min_Index != max_Index:
    # 知道下一個數字是多少
    # 目前誰比較大

    if right_Total > left_Total:
        min_Index += 1
        left_Temp += input1[min_Index]

    if right_Total < left_Total:
        max_Index -= 1
        right_Temp += input1[max_Index]


# 2 2 3 -1 1 2 3

# 10 9 0 -1 1 -1 2
