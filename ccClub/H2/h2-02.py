'''
除了to、冠詞a、an、the、少於五個字母的連接詞from、for、of、and、in不須大寫
under the dome an affair to remember
Under the Dome an Affair to Remember

a diamond is forever
A Diamond Is Forever

an end to live for 
'''
inputStr = input().split()
inputStr[0] = inputStr[0][0].upper() + "".join(inputStr[0][1::])
count = 1
# 除了to、冠詞a、an、the、少於五個字母的連接詞from、for、of、and、in不須大寫
conDic={
    "to":1,
    "a":1,
    "an":1,
    "the":1,
    "from":1,
    "for":1,
    "of":1,
    "and":1,
    "in":1,
}
for item in inputStr[1::]:
    if item in conDic and count +1 != len(inputStr):
        count += 1
        continue
    inputStr[count] = inputStr[count][0].upper() + "".join(inputStr[count][1::])
    count += 1
print(" ".join(inputStr))