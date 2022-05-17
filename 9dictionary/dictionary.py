print('1 ---------------------------')
lux = {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
print(lux)

print('2 ---------------------------')
x = {100: 'hundred', False: 0, 3.5: [3.5, 3.5]}
print(x)

print('3 ---------------------------')
x = {}
print(x)
y = dict()
print(y)
print('4 ---------------------------')
lux1 = dict(health=490, mana=334, melee=550, armor=18.72)    # 키=값 형식으로 딕셔너리를 만듦
print(lux1)

lux2 = dict(zip(['health', 'mana', 'melee', 'armor'], [490, 334, 550, 18.72]))    # zip 함수로
print(lux2)                                                            # 키 리스트와 값 리스트를 묶음

lux3 = dict([('health', 490), ('mana', 334), ('melee', 550), ('armor', 18.72)])
print(lux3)                                                  # (키, 값) 형식의 튜플로 딕셔너리를 만듦

lux4 = dict({'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72})     # dict 안에서
print(lux4)                                                           # 중괄호로 딕셔너리를 만듦

print('5 ---------------------------')
lux = {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
print(lux['health'])
print(lux['armor'])

print('6 ---------------------------')
lux = {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
lux['health'] = 2037    # 키 'health'의 값을 2037로 변경
lux['mana'] = 1184    # 키 'health'의 값을 2037로 변경
print(lux)
lux['mana_regen'] = 3.28
print(lux)

print('7 ---------------------------')
lux = {'health': 490, 'mana': 334, 'melee': 550,}
print('health' in lux)
print('attack_speed' in lux)
print('attack_speed' not in lux)

print('8 ---------------------------')
lux = {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
print(len(lux))