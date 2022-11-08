'''
醜數就是因數裡面只含有2、3和5的數（不包含1以及自己）

比方說6的因數只含有2,3，所以他就是醜數（一般來說1被我們特別歸類在醜數）

而14的因數含有7所以不是醜數

輸入為一正整數

輸出為True或是False，取決於他是不是醜數
6
True
1
True
14
False
https://judge.ccclub.io/problem/1101HW0205
'''

input1 = int(input())
while input1%5==0:
    input1 //=5
while input1%3==0:
    input1 //=3
while input1%2==0:
    input1 //=2
print(input1==1)