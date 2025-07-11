# 复制列表
lists = [1, 2, 3, 4, 5]
lists2 = lists[:]
print(lists2)  # [1, 2, 3, 4, 5]

my_foods = ['pizza', 'falafel', 'carrot cake']
# 复制列表,使用切片[:]方法,可以创建一个新的列表,并将原列表的元素复制到新列表中
# 这样,对新列表的修改不会影响原列表
# 例如,如果我们想要创建一个新的列表,包含我们朋友喜欢的食物,可以使用切片[:]方法来复制原列表
# 然后在新列表中添加新的食物项,这样就不会影响原列表了
my_foods.insert(0, '生日蛋糕')
print(f'我喜欢吃的食物是 {my_foods}')  # ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
friend_foods.append('cannoli')
print(f'我朋友喜欢吃的食物是 {friend_foods}')


# 这种是行不通的,因为不是将test的副本赋值给test2,而是将test的引用赋值给test2
# 这样,对test2的修改也会影响到test,因为它们指向同一个列表对象
test = [1, 2, 3, 4, 5]
test2 = test
print(f'赋值前是: {test}')
print(f'赋值后是: {test2}')
test2.append(66)
test.insert(0, 9)
test.append(8)
print(f'添加后数字后赋值前是: {test}')  # [0, 1, 2, 3, 4, 5, 6]
print(f'添加后数字后赋值后是: {test2}')  # [0, 1, 2, 3, 4, 5, 6]
