# 元组
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
# 尝试修改元组中的元素
# dimensions[0] = 300
# print(dimensions[0])  # 会报错，因为元组是不可变的:     tuple' object does not support item assignment

print('----type-----')
test = (1)
print(type(test))
test2 = (1, 2, 3)
print(type(test2))
test3 = ('a', 'b', 'c')
print(type(test3))
tuple = (1,)
print(type(tuple))






