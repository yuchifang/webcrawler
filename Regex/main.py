import re


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

+ one or moretimes = ca+t => match caaat cat, no match ct
* zero or moretimes = 
? matches once or zero times = home-?brew => match homebrew home-brew
{m,n} matches m n times = a/{1,3}b => 'a/b','a//b','a///b', not match ab or a////b
m,n這兩個參數都可以忽略
{0,} 等於 *, {1,} 等於 +, {0,1} 等於 ?, 最好還是使用 *,+,?

Method
match() Determine if the RE matches at the beginning of the string
search() Scan through a string, looking for any location where this RE matches.
findall() Find all substrings where the RE matches, and returns them as a list.
finditer() Find all substrings where the RE matches, and returns them as an iterator.

match() and search() return None if no match can be found. 
If they’re successful, a match object instance is returned, 
containing information about the match: where it starts and ends,
the substring it matched, and more.

redemo.py can be quite useful when trying to debug a complicated RE.
redemo.py??

'''

# 看看 backslash 怎麼唸



# 字串模式 "He"
# 對像字串 "Hello World"

result = re.match("He","Hello World") # test
# result 沒找到 return NONE

# 如果有找到 result.group() 會顯示 找到的字串
print(result)

# 其中一種 比對方式
p = re.compile('[a-z]+')

p = re.compile(r'\d+')
r = p.finditer('a12d drummers cs5drumming, 11 pipers piping, 10 lords a-leaping')
print(type(r))
for item in r:
    print(type(item))

    # 看到 Module-Level Functions
