# string issue

# input1 = list(input())
# dict = {}
# for item in input1:
#     data2 = item.lower()
#     try:
#         dict[data2]
#     except KeyError:
#         dict[data2] = 1
#     else:
#         dict[data2] = dict[data2]+1

# for data in sorted(dict):
#     if data.isalpha():
#         print(f"{data}{dict[data]}", end=" ")

#
# 2 3
# 4 7
# 3 5

# input1 = int(input())
# spaceCount = input1 - 1
# starUp = "*"
# for x in range(input1):
#     for space in range(spaceCount):
#         print(" ", end="")
#     spaceCount -= 1
#     print(starUp)
#     starUp += "**"
# spaceCount = 0
# starUp = starUp[:-2]
# for x in range(input1-1):
#     spaceCount += 1
#     for space in range(spaceCount):
#         print(" ", end="")
#     starUp = starUp[:-2]
#     print(starUp)
