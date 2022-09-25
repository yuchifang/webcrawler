import re

# print(re.match('a[bcd]*b',"acb"))
# p = re.compile('(blue|white|red)')
# m=p.sub('color', 'blue socks and red shoes')
# print(m)

p = re.compile("[^abc]")
m = p.search("bvwre")
print("m",m)

p = re.compile("[^accbc]")
m = p.search("bvwre")
print("m",m)

# print(re.match(r'From\s+', 'From age amk'))

# p = re.compile('\d+')
# m = p.finditer('12 drummers drumming, 11 pipers piping, 10 lords a-leaping')
# for n in m:
#     print(n) # None

# todo 從 Matching Characters 開使看
'''


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

# p = re.compile('[a-z]+')
# m = p.match('temp')
# print("group",m.group())
# print("start",m.start())
# print("end",m.end())
# print("span",m.span())
# todo


# 看看 backslash 怎麼唸



# 字串模式 "He"
# 對像字串 "Hello World"

# result = re.match("He","Hello World") # test
# result 沒找到 return NONE

# 如果有找到 result.group() 會顯示 找到的字串
# print(result)

# 其中一種 比對方式
# p = re.compile('[a-z]+')

# p = re.compile(r'\d+')
# r = p.finditer('a12d drummers cs5drumming, 11 pipers piping, 10 lords a-leaping')
# todo

# print(type(r))
# for item in r:
    # print(type(item))

    # 看到 Module-Level Functions
# pp = re.compile('(ab)*')
# print(pp.match('ababababab'))
# print("Hello ccClub")

