#切片
players = ['a', 'b', 'c', 'd', 'e']
print(players[0:3])  # ['a', 'b', 'c']
print(players[:2])  # 如果没有指定开头索引,python自动从头开始
print(players[2:])  # 如果没有指定结尾索引,python自动到最后结束
print(players[-3:])  # ['c', 'd', 'e'] 负数索引从后往前数-后从左到右print
print(players[-4:-1])  # ['c', 'd'] 负数索引从后往前数-后从左到右
print('-------- ')
print(players[-1:])  # ['e'] 负数索引从后往前数-后从左到右
print(players[::2])  # ['a', 'c', 'e']  步长为2,从左到右取值从[0]开始
print(players[::3])  # ['a', 'd'] 步长为3,从左到右取值从[0]开始
print('步长为-x(负数),从右到左取值')
print(players[::-1])  # ['e', 'd', 'c', 'b', 'a'] 步长为-1,从右到左取值
print(players[::-2])  # ['e', 'c', 'a'] 步长为-2,从右到左取值
