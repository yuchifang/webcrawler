import re

p = re.compile('[a-z]+')

result=p.match("8")
print(result)

# todo 從 Matching Characters 開使看
'''
[abc] == [a-c]
[a-z] 表式 全部英文小寫
在 []中 會配對任何的特殊符號 除了 "\"
[^5] 會 match 任何值 除了 5
^ 這個符號沒有任何特別意思 
[5^] 會match "5","^"

測試 下面的東西 
如果要配對特殊符號 要先在前面 加上 "\" 移除他的 特殊規則
\d
Matches any decimal digit; this is equivalent to the class [0-9].
\D
Matches any non-digit character; this is equivalent to the class [^0-9].
\s
Matches any whitespace character; this is equivalent to the class [ \t\n\r\f\v].
\S
Matches any non-whitespace character; this is equivalent to the class [^ \t\n\r\f\v].
\w
Matches any alphanumeric character; this is equivalent to the class [a-zA-Z0-9_].
\W
Matches any non-alphanumeric character; this is equivalent to the class [^a-zA-Z0-9_].

看看放到 [] 裡的差別

+ one or moretimes
* zero or moretimes
'''

# 看看 backslash 怎麼唸



# 字串模式 "He"
# 對像字串 "Hello World"

result = re.match("He","Hello World")
# result 沒找到 return NONE

# 如果有找到 result.group() 會顯示 找到的字串
if  result :
    print(result.group())