input1 = input()
stack = []
isValid = True
for item in input1:
    if item == "(":
        stack.append(item)
    if item == ")":
        if len(stack) == 0 or "(" != stack.pop():
            isValid = False
            break
print(isValid and len(stack) == 0)
