# 0 <= i < j < k <= len(nums) - 1
# 陣列常長度 大於 .
# nums[i] + nums[j] == nums[k]
# 任前兩項 相加 等於 某一項
# 計算幾組符合條件

# 1 2 3 6 = 1
# 1 3 4 8 2 6 = 2


data = [int(item) for item in input().split(" ")]
cache = {}


def isVaild(data):
	count = 0
	for item in data:
		if data.index(item)<2:
			continue
		cache ={}
		for index in range(0,data.index(item)):
			dataListItem = data[index]
			if dataListItem in cache:
				cache[dataListItem]	= cache[dataListItem]+1 
			else:
				cache[dataListItem]	= 1

			if index <1:
				continue
			if item - dataListItem in cache :
				if dataListItem == item - dataListItem and cache[dataListItem] ==1 :
					continue
				count+=1
				
				break
		
		
	print(count)

isVaild(data)
# 1 1 2 4 8
# 1
# 1 3 4 8 2 6
# 2
# 1 2 3 6
# 1
