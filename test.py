# 陳詩雅,152,O 潘姿怡,157,AB 林亭莉,161,B
data = [item.split(",") for item in input().split()]
input2 =input()
for item in data:
    if input2==item[0]:
        print([item[1],item[2]])