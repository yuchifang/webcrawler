'''

0 = 0
1 = 1
-5 -4 -3 -2 -1 = 5
-1 0 1 2 3 4 = 6
1 2 3 4 5 6 7 8 = 8 
1 2 3 5 6 7 8 = 4
5 4 3 2 1 = 0
3 2 3 1 = 2
1 2 3 4 5 1 2 = 5
1 2 1 2 3 4 5 = 5

10 20 30 => 3
30 20 10 => 1
1 1 1 1 => 1
-1 -1 -1 0 => 2
0 1 1 1 => 2
'''

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