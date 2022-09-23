'''
戰術筆,85
傘繩31公尺,99
防刀衣,4500
軍用指北針,350
多功能鉗,900
尖嘴鉗,80
打火棒,38
迷你太陽能手電筒,200
求生毯,10
end
'''
'''
Python 自動化的樂趣：搞定重複瑣碎&單調無聊的工作(第二版),537
Effective Python中文版：寫出良好Python程式的90個具體做法(第二版),458
end
'''
dataList = []
data = input()
while  "end" != data :
    dataList.append(data.split(","))
    data = input()
print(dataList)