#组织列表
print('使用sort()方法来永久排序-----------------')
cars = ['bmw','audi','toyota','subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

#使用sorted()函数来临时排序
print('使用sorted()来临时排序--------------')
cars1 = ['bmw','audi','toyota','subaru']
print(f'\n原来的顺序是:')
print(cars1)
print(f'\n现在的顺序是:')
print(sorted(cars1))
print(f'\n再次打印之前的列表')
print(cars1)
print(f'\n按照相反的顺序打印')
print(sorted(cars1,reverse=True))


#倒着打印列表
print('倒着打印列表---------------')
test = ['ok','dad','apple','aitcon','question','pos']
print(f'\n原列表:\n{test} ')
print(f'\n按字母临时排序: {sorted(test)}')
print(f'\n原列表:\n{test} ')
test.reverse()             #不是按字母顺序相反顺序排列的,只是反转列表元素的排列顺序----reverse()可永久修改位置,恢复需要再一次调用reverse()
print(f'\n反转列表排列元素(单纯倒着打印)\n{test}\n')



#确定列表的长度
cars2 = ['bmw','audi','toyota','subaru']
print('确定列表的长度-------------------')
print(f'\n目前列表还有" {len(cars2)} "个元素')

from pypinyin import pinyin, lazy_pinyin, Style

#小练习
print('小练习-----------------------------------------------')
travel = ['张家界','西藏','新疆','意大利','华山','黄山','三亚','马尔代夫','毛里求斯','普吉岛']
print(f'\n这是原列表: \n {travel} ')
print('\n这是排序后的列表: ')
print(f'{sorted(travel, key=lambda x: lazy_pinyin(x))}')             #来自deepseek搜索汉字拼音排序
print(f'\n这是原列表: \n {travel} ')

print(f'\n 这是字母相反的排序: \n {sorted(travel, reverse = True, key=lambda x: lazy_pinyin(x))}')

print(f'\n这是原列表: \n {travel} ')


print('\n')
print('使用reverse()打印列表---------------')
print(f'\n这是原列表: \n {travel} ')
travel.reverse()
print(f'\n这是修改后的列表 \n{travel} ')
travel.reverse()
print(f'\n重新修改为原列表:\n {travel}')


print('\n')
print('使用sort()打印列表---------------')
print(f'\n这是原列表: \n {travel} ')
travel.sort(key=lambda x: lazy_pinyin(x))
print(f'\n这是修改后的列表:\n {travel}')

travel.sort(reverse = True, key=lambda x: lazy_pinyin(x))
print(f'\n 使用逆序排列顺序后的列表是: \n{travel}')

print(f'\n再次打印原列表:\n{travel},看到顺序已改变')

print(f'\ntravel中一共有" {len(travel)} "个元素')




#小练习3-10
print('----------小练习3-10-----------')
mountions = ['华山','泰山','嵩山','恒山','衡山']
print(f'原列表是: {mountions} ')

print(f'访问第一个元素: {mountions[0]} ')
print(f'访问第三个元素: {mountions[2]} ')
print(f'访问第四个元素: {mountions[-1]} ')
mountions.append('黄山')
print(f'再添加一座山后是: {mountions}')
mountions.append('雁荡山')
mountions.append('庐山')
print(f'添加三山后是: {mountions}')
mountions[2] = '峨眉山'
print(f'嵩山去过了,改为去峨眉山后的列表是: {mountions}')








# #取自kimi
# print('---------------test_取自kimi----------------')
# from pypinyin import lazy_pinyin

# # 待排序的汉字列表
# hanzi_list = ["苹果", "香蕉", "橙子", "西瓜", "梨"]

# # 按拼音首字母排序
# sorted_list = sorted(hanzi_list, key=lambda x: lazy_pinyin(x)[0][0])

# print(sorted_list)
# # 反转排序结果
# sorted_list.reverse()           #另一种思路,先按首字母排序,再倒着打印

# print(sorted_list)  # 输出：['梨', '西瓜', '香蕉', '橙子', '苹果']

# print(f'\nhanzi_list中一共有" {len(hanzi_list)} "个元素')

print('---------------------要去的河流------------------')
river = ['长江','黄河','珠江','密西西比河','多瑙河','莱茵河']
print(river)
print(f'我已经去过的河流有 {river[1]}')
#print(f'我没有去过的河流有 {river[1]}')
print(f'我没有去过的河流有 {river[0] , river[2] , river[3] , river[-2] , river[-1]}')
print(f'我将来还要去看这些河流: "伏尔加河"')
river.append('伏尔加河')
print(f'我要去的地方 {river}')
print('密西西比河太远了,改为去')
river[3] = '京杭大运河'
print(f'现在要去的河流 {river}')
print('好像澜沧江没去过,去一下')
river.insert(3,'澜沧江')
print(f'现在要去的河流 {river}')
print('黄河去过了,不去了')
del river[1]
print(f'现在要去的河流 {river}')
print('钱不太够,得去掉一个,先留着,将来和对象一起去')
pop_list = river.pop(2)     #river.pop() 默认是最后一个元素
print(f'把 {pop_list} 这个留到明年吧! ')
print(river)
re = '京杭大运河'
re_list = river.remove(re)
print(f'{re}不适合旅游')
print(f'现在要去的河流 {river}')

print(f'太乱了排下序 {sorted(river)}')  #sorted(x)    是函数,用来临时排序
print(f'算了,还是原来的吧!')
print(f'现在要去的河流 {river}')
print(f'重新来拍下序吧')
river.sort()
print(f'现在要去的河流 {river}')
print('反过来旅游吧')
river.sort(reverse = True)      #x.sort()  是方法 reverse = True  倒序
print(f'现在要去的河流 {river}')
leng = len(river)
print(f'一共要去{leng}个地方 ')

