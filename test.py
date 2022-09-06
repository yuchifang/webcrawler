# sampleList = [{"name1":"Dan"},{"name2":"Sam"},{"name3":"KID"}]
# for x,y in sampleList:
# 	print(x,y)


thisdict = {
	"brand": "Ford",
	"year" : 2020,
}
print( thisdict.items())
list = thisdict.items()
for x,y in list:
    print(x,y)