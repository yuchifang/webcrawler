letGo = True

dicCValue = {}
dicEValue = {}
while letGo:
    input1 = input().split()
    if input1[0] == 'I':
        if input1[1] in dicEValue or input1[2] in dicCValue:
            print('[fail]')
            continue
        dicEValue[input1[1]] = input1[2]
        dicCValue[input1[2]] = input1[1]
        print('[succeed]')
    if input1[0] == 'C':
        try:
            input1[1] in dicEValue
            print(dicEValue[input1[1]])
        except KeyError:
            print('[fail]')
    if input1[0] == 'E':
        try:
            input1[1] in dicCValue
            print(dicCValue[input1[1]])
        except KeyError:
            print('[fail]')
    if input1[0] == 'Q':
        letGo = False
        break
