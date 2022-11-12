'''


4 3 2 1
b b a c

2 4 1 3

----------------

1 2 3 4 5 6
c c c l u b

6 1 4 5 2 3


看看這個code 依據題目要求結果如何
6 4 3 2 1 7
c c c l u b

7 6 2 1 4 3

1 2 3 4 5
a b c d z

5 4 3 2 6 7 8 9
z d c b a a b c

6 2 3 4 5 7 8 9

5 4 3 2 7 8 9 10 11 11
a b c d 

7 2 3 4 10 5 11 8 9 11
'''

Number_List = [int(item) for item in input().split()]
Level_List = [item for item in input().split()]
level_dic = {}
totalLength = len(Level_List)


for index, item in enumerate(Number_List):
    level = Level_List[index]

    if level in level_dic:
        level_dic[level].append(int(item))
    else:
        level_dic[level] = [int(item)]

all_level_sorted = sorted(list(set({*level_dic})))  # 已排列好的 key

returnArr = []
outSideCount = 0
while outSideCount < totalLength:
    def appendFun():
        global outSideCount
        global all_level_sorted

        for item in all_level_sorted:
            if item in level_dic and len(level_dic[item]) > 0:
                returnArr.append(str(level_dic[item].pop(0)))
                outSideCount += 1

    appendFun()
    all_level_sorted = all_level_sorted[::-1]
print(" ".join(returnArr))

'''
5 4 3 2 6 7 8 9
z d c b a a b c

6 2 3 4 5 9 8 7
'''
