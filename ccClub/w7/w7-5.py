'''
1 2 3
4 5 6
7 8 9
'''
data=[int(item) for item in input().split()]
answer = [[1,2,3],[1,4,7],[4,5,6],[7,8,9],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
output="F"
for item in answer:
    if item == data:
        output = "T"
        break
print(output)