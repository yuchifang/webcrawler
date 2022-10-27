'''
22:40
23:40
Y

20

15:00
23:59
N

360

每半小時 為20元
Y 停車證 10元
Y less 30 minute free
'''
startTime = [int(item)for item in input().split(":")]
endTime = [int(item)for item in input().split(":")]
haveCard = input()
if haveCard =="Y":
    haveCard = True
else:
    haveCard = False
startTimeMinute = startTime[0] * 60 + startTime[1]
endTimeMinute = endTime[0] * 60 + endTime[1]

def HowMuchToPay(startTimeMinute,endTimeMinute,haveCard):
    totalTime = endTimeMinute - startTimeMinute
    if totalTime == 0:
        return 0
    if haveCard and totalTime < 30:
        return 0
    
    add = totalTime % 30
    count = totalTime // 30
    if add != 0:
        count += 1

    if haveCard:
        return count * 10
    else:
        return count * 20


print(int(HowMuchToPay(startTimeMinute,endTimeMinute,haveCard)))
