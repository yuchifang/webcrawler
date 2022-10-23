input1 = [int(item) for item in input().split()]
input2 = [int(item) for item in input().split()]

listInput = []
for row in range(input1[0]):
    [listInput.append(int(item)) for item in input().split()]

count = 0
for item in listInput:
    if count+1 == input2[1]:
        print(item, end="")
    else:
        print(item, end=" ")
    count += 1
    if count == input2[1]:
        print()
        count = 0

    # for row in range(input2[0]):

    # for col in range(input2[1]):
    #     if col == input2[1] - 1:
    #         print(listInput.pop(0), end="")
    #     else:
    #         print(listInput.pop(0), end=" ")
    # print()
