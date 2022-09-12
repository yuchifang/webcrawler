def multi_sort(s):
    return (len(s), s.count("s"))

print(set({"a":1,"c":2,"d":6,"w":4,"cc":5}))
print(set((1,2,3,4,5)))
print(set([2,3,4,5]))

mylist = ["pen", "pineapple", "pineapple", "applepens", "apple"]

print(sorted(mylist, key=multi_sort, reverse=True))
mylist.sort(key=multi_sort, reverse=True)
print(mylist)
# ['applepens', 'pineapple', 'pineapple', 'apple', 'pen']
