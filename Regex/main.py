import re

p = re.compile('[a-z]+')

result=p.match("8")
print(result)

'''
[abc] == [a-c]
[a-z] 表式 全部英文小寫
在 []中 會配對任何的特殊符號 除了 "\"
[^5] 會 match 任何值 除了 5
^ 這個符號沒有任何特別意思 
[5^] 會match "5","^"
'''





# 字串模式 "He"
# 對像字串 "Hello World"

result = re.match("He","Hello World")
# result 沒找到 return NONE

# 如果有找到 result.group() 會顯示 找到的字串
if  result :
    print(result.group())