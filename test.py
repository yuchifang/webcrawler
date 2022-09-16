def square_check(x):
	if x ==1:
		print(1)
		return 1
	for item in range(1,x):
		if item*item >= x:
			print((item-1)*(item-1))
			return (item-1)*(item-1)

n = int(input())
square_check(n)
