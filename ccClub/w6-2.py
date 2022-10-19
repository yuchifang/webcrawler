input1 = [int(item) for item in input().split()]
input2 = [int(item) for item in input().split()]

listInput = []
for row in range(input1[0]):
    [listInput.append(int(item)) for item in input().split()]

for row in range(input2[0]):
    for col in range(input2[1]):
        if col == input2[1] - 1:
            print(listInput.pop(0), end="")
        else:
            print(listInput.pop(0), end=" ")
    print()
