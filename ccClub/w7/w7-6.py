'''
輸入有數行。

第一行包含數個整數，有正有負，表示原先帳本上的內容。

接下來數行各包含一個字母（指令的類型）以及一個數字，以空白為間隔。

若輸入為 "a 4"，請在帳目中加入4 這個數字。

若輸入為 "r 204"，請從帳目中刪除第一次出現 204 這個數字，若帳本中沒有 204 這個數字，則略過這個指令。

若輸入為 "p -1"，請從帳目中刪除 index 為 -1 的帳目，p 指令後如果是負數，保證是 -1。

若輸入為 "p 2" ，請從帳目中刪掉 index 為 2 的帳目，若 index 2 不存在帳本中，則略過這個指令。

若輸入為 "q 4" ，請結束輸入的部分，並印出 index 為 4 的內容，以及所有帳目的平均數；若該 index不存在，請輸出 Error ，並且不需要輸出平均數。


##
1 2 3 4 5 6 7
a 8
r 2
p -1
q 4

6
4

##
10 9 8 7 6 5 4 3 2 1
q 10

Error
'''
memo = [int(item) for item in input().split()]
run = True
while run:
    inputAlp = input().split()
    if inputAlp[0] == "q":
        run = False
        indexCount = int(inputAlp[1])
        try:
            print(memo[indexCount])
            print(sum(memo)//len(memo))
        except IndexError:
            print("Error")
        finally:
            break
    if inputAlp[0] == "a":
        memo.append(int(inputAlp[1]))
    if inputAlp[0] == "r":
        if int(inputAlp[1]) in memo:
            memo.remove(int(inputAlp[1]))
    if inputAlp[0] == "p":
        if int(inputAlp[1]) == -1:
            memo.pop(-1)
            continue
        if len(memo) <=int(inputAlp[1]):
            continue
        memo.pop(int(inputAlp[1]))


