def social_distance(x, y):
	if x.strip() == "室外" and int(y) < 100:
		print("請維持社交距離")
	if x.strip() == "室內" and int(y) < 150:
		print("請維持社交距離")
x=input().split(",")

social_distance(x[0],x[1])