# 4-10
games = ['lol', '王者荣耀', 'dota2', 'csgo', 'apex']
print(f'The first three items in the list are: {games[:3]}')
print(f'Three items from the middle of the list are: {games[1:4]}')
print(f'The last three items in the list are: {games[-3:]}')

# 4-11
print('4-11---------------------------------------------------------------')
my_pizza = ['big_pizza', 'small_pizza', 'middle_pizza']
friend_pizza = my_pizza[:]
my_pizza.append('玛格丽特披萨')
my_pizza.insert(1,'香肠披萨')
friend_pizza.append('海鲜至尊披萨')
friend_pizza.insert(2,'芝加哥深盘披萨')
print(f'My favorite pizzas are {my_pizza}')
print(f'My friend favorite pizzas are {friend_pizza}')



print('4-12---------------------------------------------------------------')
my_foods = ['pizza', 'falafel', 'carrot cake']
# 复制列表,使用切片[:]方法,可以创建一个新的列表,并将原列表的元素复制到新列表中
# 这样,对新列表的修改不会影响原列表
# 例如,如果我们想要创建一个新的列表,包含我们朋友喜欢的食物,可以使用切片[:]方法来复制原列表
# 然后在新列表中添加新的食物项,这样就不会影响原列表了
my_foods.insert(0, '生日蛋糕')
friend_foods = my_foods[:]
friend_foods.append('cannoli')
#print(f'我朋友喜欢吃的食物是 {str(friend_foods)}')    #怎样将输出结果为我朋友喜欢吃的食物是 生日蛋糕', 'pizza', 'falafel', 'carrot cake', 'cannoli

print('-------------')
for my_food in my_foods:
    print(f'我喜欢吃的食物是: {my_food}')
print('------friend-------')
for friend_food in friend_foods:
    print(f'我朋友喜欢吃的食物是: {friend_food}')
    
