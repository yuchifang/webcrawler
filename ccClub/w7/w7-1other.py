k = [ int(i) for i in input().split() ]
increment = 0 #未被清空前算到的最大連續
combo = 0 #現在計算的最大連續
lenk= len(k)
for i in range( 1, lenk ):
    if k[i] == k[i-1]+1 and combo == 0:
        combo += 2
    elif k[i]== k[i-1]+1:
        combo += 1
#不符合連續，先把目前最大連續存起來，再歸零重新算
    else:
        increment = max(increment,combo)
combo = 0
#5只有一個數字也算連續1
if lenk == 1 :
    increment +=1
print(max(increment,combo))