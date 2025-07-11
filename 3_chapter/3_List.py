#列表

bicycles = ['trek','cannondale','REDLINE','specialized']
print(bicycles)
print(bicycles[0].title())
print(bicycles[3])
print(bicycles[0].upper())
print(bicycles[2].lower())
print(bicycles[-1])         #显示最后一个可以-1索引表示,以此类推
print(bicycles[-2])

message = f'My first bicycle was a {bicycles[2]}'
print(message)




names = ['张镇南','吴心星','张豪康']
print(names[0])
print(names[1])
print(names[-1])
welcome = f'{names[1]} 你好,今天认识你很高兴!'
welcome2 = f'{names[-1]} 你好,今天认识你很高兴!'
welcome1 = '今天和你一起玩很快乐'
print(welcome)
print(welcome2)
print(f"{names[1]} {welcome1}")
print(f"{names[-1]} {welcome1}")

Commuting = ['自行车','汽车','电动车']


print(f'我最喜欢的通勤方式是{Commuting[1]}')


#修改,添加和删除列表
print('修改,添加和删除列表-----------')
motorcycle = ['honda','yamaha','suzuki']
print(motorcycle)
motorcycle[2] = '铃木'
print(motorcycle)

motorcycle.append('ducati')             #给列表添加元素 append() 附加
print(motorcycle)

list = []
list.append('汽车')
list.append('computer')
list.append('美女')
print(list)
list[1] = 'phone'
print(list)
list.insert(0, '一个小目标')
print(list)
list.insert(2,'BTC')
list.insert(3,'老婆')
print(list)
del list[0]
print(list)

#使用pop方法删除元素
print('使用pop方法删除元素-----------------------')
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
motorcycles1 = motorcycles.pop()
print(motorcycles)
print(motorcycles1)

print(f"The last motorcycle I owned was a {motorcycles1.title()} !")

popend = motorcycles.pop(1)
print(popend)

print('我买不起的摩托车是:'+popend.title())


#根据值删除元素
print('根据值删除元素------------------')
motorcycles = ['honda','yamaha','suzuki','ducati']
moto_del = motorcycles.remove('yamaha')
print(motorcycles)


print('-------1--------')
moto_1 = ['honda','yamaha','suzuki','ducati']
print(moto_1)
too_moto = 'yamaha'          #创建变量可以保留值
moto_1.remove(too_moto)

print(moto_1)
print(f'\nA {too_moto.title()} is expensive for me')

#聚会邀请名单
print('聚会邀请名单')
list_name = ['张天飞','吴心星','张豪康','吴树恒','李正阳','魏江硕','李柄辉']
birthday = '你好,今天是我生日,我想邀请你共进晚餐'
print(f'\n"{list_name[0]}" 你好,今天是我生日,我想邀请你共进晚餐')
print(f'\n"{list_name[2]}" 你好,今天是我生日,我想邀请你共进晚餐')
print(f'\n"{list_name[4]}" 你好,今天是我生日,我想邀请你共进晚餐')
print('\n"'+list_name[3]+'" ' + birthday)
print('\n"'+list_name[-2]+'" ' + birthday)
print('\n"'+list_name[1]+'"' , birthday)
print('\n"'+list_name[-1]+'"' , birthday)
print('\n李正阳在北京无法赴约')
list_name.remove('李正阳')
list_name.append('潘炬豪')
print('\n张天飞有事无法赴约,让他朋友张镇南来')
list_name[0] = '张镇南'
print('\n酒店找到了一个更大的餐桌,可以邀请更多的人')
list_name.insert(3,'郭豪')
list_name.insert(3,'栗广正')
print('\n')
print(list_name)
print('\n酒店找的桌子是坏的无法使用,只能邀请两个人0.0--------------------------\n')
print(list_name)
no = list_name.pop()
print(f'\n"{no}" 抱歉,桌子不够用无法邀请你一起共进晚餐了')
print(list_name)
no = list_name.pop()
print(f'\n"{no}" 抱歉,桌子不够用无法邀请你一起共进晚餐了')
print(list_name)
no = list_name.pop()
print(f'\n"{no}" 抱歉,桌子不够用无法邀请你一起共进晚餐了')
print(list_name)
no = list_name.pop()
print(f'\n"{no}" 抱歉,桌子不够用无法邀请你一起共进晚餐了')
no1 = list_name.pop(0)
print(f'\n"{no1}" 抱歉,桌子不够用无法邀请你一起共进晚餐了')
no1 = list_name.pop(2)
print(list_name)
print(f'\n"{no1}" 抱歉,桌子不够用无法邀请你一起共进晚餐了')
no1 = list_name.pop(2)
print(f'\n"{no1}" 抱歉,桌子不够用无法邀请你一起共进晚餐了')
print(f'\n{list_name[0]} 您目前还在邀请之列')
print(f'\n{list_name[-1]} 您目前还在邀请之列')
del list_name[0]            #del list_name              可直接删除该列表
del list_name[-1]
print('\n')
print(list_name)
