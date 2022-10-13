data = int(input())
itemList = []
for item in range(1,data):
    if data%item==0:
        itemList.append(data//item)
        itemList.append(item)

for item in itemList:
# print(itemList)
# if 2 in itemList:
#     itemList.remove(2) 
# if 3 in itemList:
#     itemList.remove(3)
# if 5 in itemList:
#     itemList.remove(5)
print(itemList)

if len(itemList)>1:
    print(False)
else:
    print(True)