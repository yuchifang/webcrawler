# listExample = [1, 2, 3, 4, 5, 6, 7]
# index = listExample.index(1)
# print(index)

x = {'a':1,'b':2}
y = {'b':3,'d':4}

z={**x,**y}
print(z)


newZ = x.copy()
newZ.update(y)
print(newZ)