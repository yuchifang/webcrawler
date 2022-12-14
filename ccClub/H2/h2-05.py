'''
在他的「室外社交距離內(1m)」，是否存有高風險對象，如果有的話，警報器會提醒他，並告知其不安全的方位。

由上到下依序指的是位於迷果
東、西、南、北的人的資訊，
代碼總共分為三個部分:
前三個英文字母代表此人近一個月去過的國家，
後面兩個用逗號隔開的字母代表這個人目前的 (x,y)位置 ( 單位為cm ),
最後一個大寫字母代表的是是否與染疫者的足跡重疊。
是的話就是 T,不是就是 F。

舉例來說 TWN20,36T 就代表此人近一個月在台灣，
位置在 x = 20 (cm) , y = 36 (cm),
T 代表曾經跟染疫者接觸。

警報器會檢查與自己距離小於「室外社交距離」的人中，
是否有人曾經與染疫者接觸，亦或是來自國外，如果沒有的話則輸出 ”Safe” ;
 如果有的話，警報器會先輸出 ”Alarm”,
 接下來的若干行會將所有不安全的路徑輸出 
 ( 與染疫者足跡重疊或來自外國的方位都可以，
 假設只有前方的人是不安全的,則輸出North, 如果前方和左方的人是不安全的則輸出 North (換行) East ;
  若皆沒有安全路徑，則輸出 " Virus in your area " )



input

共有5行,
第1行有兩個數,用逗號隔開,為迷果現在的位置資訊。

接下來的4行為迷果東西南北的人的資訊代碼,
會有3個英文字代表國家代碼,
兩組用逗號隔開的數字代表位置,
最後加上T或F代表過去是否與染疫者的足跡一致。

output
共n行,(n<=4)
第1行,輸出Alarm或Safe 
(如果是四方都是危險則直接輸出 "Virus in your area")
接下來的n-1行(n-1<4),
如果警報器有被啟動，
且並非所有路徑都不安全的情況
(不安全路徑總數大於0且小於4 ),
則輸出不安全的路徑(按照東西南北的順序)。


input
0,0
TWN20,36F 東
TWN-1,2F 西
TWN3,-3F 南
TWN89,3F 北

output
Safe

-------------------------
input
10,10
AFG400,245F
TWN3,50T
USA27,9F
TWN200,200T

output
Alarm
West
South
--------------------------

input
10,10
USA11,10F
TWN9,10T
ALB10,9F
TWN10,11T

output
Virus in your area
---------------------------


'''

# 國外 或是有與確診者接觸

pos = [int(item) for item in input().split(",")]
Alert_Str_List = []
posDic = {
    0: "East",
    1: "West",
    2: "South",
    3: "North"
}

for index in range(4):
    isForeign = False
    isVirus = False
    inRange = False
    data = input()
    if data[0:3] != "TWN":
        isForeign = True
    if data[-1::] == "T":
        isVirus = True
    curr_Pos = [int(item) for item in data[3:-1:].split(",")]
    if ((curr_Pos[0]-pos[0])**2+(curr_Pos[1]-pos[1])**2)**0.5 < 100:
        inRange = True
    if inRange and (isForeign or isVirus):
        Alert_Str_List.append(posDic[index])

returnLength = len(Alert_Str_List)
if returnLength == 0:
    print("Safe")
elif 4 > returnLength and returnLength > 0:
    print("Alarm")
    [print(item) for item in Alert_Str_List]
else:
    print("Virus in your area")
