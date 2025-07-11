#1. 生成1-20的数字列表并打印
for value in range(1, 21):
    print(value)

#2. 生成1-1M的数字列表打印(数字太大改为10k)
for value1 in range(1, 10001):
    print(value1)

#3. 生成1M并求和(数字太大改为10k)
sum_value2 = sum(value2 for value2 in range(1, 10001))
print(sum_value2)
print(min(value2 for value2 in range(1, 10001)))  #输出最小值1
print(max(value2 for value2 in range(1, 10001)))  #输出最大值10000  
#print(sum(value2 for value2 in range(1, 10001)))  #输出总和50005000

#4. 生成包含1-20的奇数列表并打印
for value3 in range(1, 21, 2):
    print(value3)

#5. 生成包含3~30中能被3整除的数字列表并打印
for value4 in range (3, 31 , 3):
    print(value4)

#6. 生成将一个数的立方值并打印
for value5 in range(1, 11):
    print(value5**3)

#6.5 生成一个数的立方解析成列表并打印

li = []
print('---')
for value6 in range(1, 11):
    
    li.append(value6**3)
print(li)
print('---')

list2 = [value6**3 for value6 in range(1, 11)]
print(list2)


