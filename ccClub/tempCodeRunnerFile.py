data = int(input())
for item in range(1, data):
    if item * item < data:
        print(item*item)
    else:
        break