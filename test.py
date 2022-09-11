def multi_sort(s):
    return (len(s), s.count("s"))


mylist = ["pen", "pineapple", "pineapple", "applepens", "apple"]

print(sorted(mylist, key=multi_sort, reverse=True))
mylist.sort(key=multi_sort, reverse=True)
print(mylist)
# ['applepens', 'pineapple', 'pineapple', 'apple', 'pen']
