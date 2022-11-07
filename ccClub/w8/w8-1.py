# y x
data = input().split()
count = 0
x = 0
while len(data) > 0:
    count += 1
    data = input().split()
    if "小明" in data:
        x = data.index("小明")
        break
    pass
print(f"({count}, {x})")
