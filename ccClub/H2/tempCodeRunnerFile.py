rate = int(input())
dictStaff = {}
go = True
listName = []
while go:
    data = input().split()
    if data[0] == "end":
        go = False
    else:
        listName.append(data[0])

        dictStaff[data[0]] = data[1::]


def getDiffItem(Lst1, Lst2):
    returnList = []
    for item in Lst2:
        if item not in Lst1:
            returnList.append(item)
    return returnList


def getRecommendItem(output_Name):
    global rate
    printList = [output_Name]
    current_List = dictStaff[output_Name]
    current_List_Length = len(current_List)
    repeat_List = []
    for key in dictStaff:
        if key == output_Name:
            continue
        repeat_List = [item for item in dictStaff[key]
                       for target_Item in dictStaff[output_Name] if target_Item == item]
        diff_List = getDiffItem(dictStaff[output_Name], dictStaff[key])
        if (len(repeat_List) / current_List_Length)*100 >= rate:
            printList.extend(diff_List)
    answerList = []
    [answerList.append(item) for item in printList if item not in answerList]
    return answerList


for outputName in listName:
    print(" ".join(getRecommendItem(outputName)))