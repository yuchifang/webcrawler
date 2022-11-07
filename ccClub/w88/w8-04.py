'''
4
8
16
120
True
'''

'''
4
8
16
40
False
非正整數、0、無解、無限多解,該題目都不合格，輸出 False。
'''
"x+y=16"
"4x+8y=120"

'''
  
x = 16 - y
4x # 64 - 4y

64 - 4y + 8y = 120
x + y = 16
4x + 8y = 120

'''
x = 0
y = 0
equation1 = [(1,x),(1,y),16]
equation2 = [(4,x),(8,y),120]
diff=equation2[0][0]/equation1[0][0]
equation1[0][0] * diff

equation1[1][0] * diff # y
# y X equation1[1][0] * diff + equation2[1][0] = equation2[2]-equation1[2] * diff
