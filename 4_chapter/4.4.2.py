# 遍历列表
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("The first three items in the list are:")
for player in players[:3]:
    print(player.title())  # title()首字母大写
print("The last two items in the list are:")

for player in players[-2:]:
    print(player.title())
