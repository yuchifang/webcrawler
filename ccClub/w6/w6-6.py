letGo = True

# set
# zfill(4)
# dic ok
# zfill(3)
# count ok
# zfill(4)

# list
letGo = True
bookOrder = []
uniBookSet = {""}
repeatNameCountDict = {}
bookTotalCount = 0
while letGo:
    newBook = input()
    bookTotalCount += 1
    if newBook == "0":
        letGo = False
        break
    uniBookSet.add(newBook)

    if newBook not in bookOrder:
        bookOrder.append(newBook)

    if newBook in repeatNameCountDict:
        totalBook = len(repeatNameCountDict[newBook]) + 1
        repeatNameCountDict[newBook].append(
            [len(uniBookSet)-1, totalBook, bookTotalCount])
    else:
        repeatNameCountDict[newBook] = [[len(uniBookSet)-1, 1, bookTotalCount]]


for item in bookOrder:
    print(f"{item}", end="")
    uniBookCount = repeatNameCountDict[item][0][0]
    for item in repeatNameCountDict[item]:
        print(" ", end="")
        print(str(uniBookCount).zfill(3) +
              str(item[1]).zfill(3)+str(item[2]).zfill(4), end="")
    print()
