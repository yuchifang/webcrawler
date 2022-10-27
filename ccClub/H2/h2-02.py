inputStr = input().split()
inputStr[0] = inputStr[0][0].upper() + "".join(inputStr[0][1::])
count = 1
for item in inputStr[1::]:
    print(item)
    count += 1

