# 遍历整个列表
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f'{magician.title()}, that was a great trick!')  #title()方法将首字母大写
    print(f'I can\'t wait to see your next trick, {magician.title()}.')
    print(f'我期待你的下一次表演, {magician.title()}. \n')

print('Thank you, everyone. That was a great magic show!')  #结束语
print('感谢大家,这是一场精彩的魔术表演!')

# 4.2--------------------
# message = 'Hello Python world!'
#     print(message)


pizzas = ['big_pizza', 'medium_pizza', 'small_pizza']
for pizza in pizzas:
    print(f'我喜欢 {pizza}!')
print('I really like pizza!')

pets = ['dog', 'cat', 'rabbit']
for pet in pets:
    print(f'A {pet} would make a great pet!')
print('Any of these animals would make a great pet!')
print('他们都是很好的宠物!')



# 4.3--------------------数值列表
for value in range(1, 5):
    print(value)

print('------------------')
for value in range(1, 6):
    print(value)

print('--------0.0----------')
for value in range(6):
    print(value)
print('--------list()----------')
#使用函数list()来将range()的结果转换为列表
numbers = list(range(1, 6))  #range()函数生成一个从1到5的数字序列
print(numbers)  #输出列表[1, 2, 3, 4, 5]


even_numbers = list(range(2, 11, 2))
print(even_numbers)  #输出列表[2, 4, 6, 8, 10]
#range(2, 11, 2)表示从2到10的偶数，步长为2


# 4.3.2--------------------
#平方数列表
print('平方数列表')
squares = []
for ff in range(1 , 11):
    print(ff)  #输出1到10的数字
    square = ff ** 2  #平方
    squares.append(square) #将平方数添加到列表中
print(squares)

print('列表解析4.3.4--------------------')
squares2 = [ff ** 2 for ff in range(1, 11)]
print(squares2)