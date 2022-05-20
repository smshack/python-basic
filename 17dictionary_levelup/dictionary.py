
print('1 update setdefault(키, 기본값) ---------------------------')
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.setdefault('e')
print(x)

x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.update(a=90)
print(x)
x.update(e=50)
print(x)
x.update(a=900, f=60)
print(x)


y = {1: 'one', 2: 'two'}
y.update({1: 'ONE', 3: 'THREE'})
print(y)
y.update([[2, 'TWO'], [4, 'FOUR']])
print(y)

y.update(zip([1, 2], ['one', 'two']))
{1: 'one', 2: 'two', 3: 'THREE', 4: 'FOUR'}

print('2 pop popitem clear ---------------------------')
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
p=x.pop('a')
print(x)
print(p)
print(x.pop('z', 0))
del x['b']
print(x)
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
t=x.popitem()
print(t)
print(x)
x.clear()
print(x)

print('3 get ,items ,keys ,values---------------------------')
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
print(x.get('a'))
print(x.items())
print(x.keys())
print(x.values())

print('4 dict.fromkeys ,items ,keys ,values---------------------------')

keys = ['a', 'b', 'c', 'd']
x = dict.fromkeys(keys)
y = dict.fromkeys(keys, 100)
print(x)
print(y)

print('5 for ------------------------------')
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
for i in x:
     print(i, end=' ')

x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
for key, value in x.items():
     print(key, value)

for key, value in {'a': 10, 'b': 20, 'c': 30, 'd': 40}.items():
    print(key, value)

x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
for key in x.keys():
     print(key, end=' ')

x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
for value in x.values():
     print(value, end=' ')
print()
print('6 표현식 사용 ------------------------------')
keys = ['a', 'b', 'c', 'd']
x = {key: value for key, value in dict.fromkeys(keys).items()}

print(dict.fromkeys(keys))
print(dict.fromkeys(keys).items())
print(x)
print({key: 0 for key in dict.fromkeys(['a', 'b', 'c', 'd']).keys()})
print({value: 0 for value in {'a': 10, 'b': 20, 'c': 30, 'd': 40}.values()})

print('7 표현식if 사용 ------------------------------')
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x = {key: value for key, value in x.items() if value != 20}
print(x)

print('8 딕셔너리 중첩 사용 ------------------------------')
terrestrial_planet = {
    'Mercury': {
        'mean_radius': 2439.7,
        'mass': 3.3022E+23,
        'orbital_period': 87.969
    },
    'Venus': {
        'mean_radius': 6051.8,
        'mass': 4.8676E+24,
        'orbital_period': 224.70069,
    },
    'Earth': {
        'mean_radius': 6371.0,
        'mass': 5.97219E+24,
        'orbital_period': 365.25641,
    },
    'Mars': {
        'mean_radius': 3389.5,
        'mass': 6.4185E+23,
        'orbital_period': 686.9600,
    }
}
 
print(terrestrial_planet['Venus']['mean_radius'])    # 6051.8
print(terrestrial_planet)
print(terrestrial_planet['Venus'])

print('9 딕셔너리 할당과 복사 ------------------------------')
x = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
y = x
print(x is y)
y['a'] = 99
print(x)

x = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
y = x.copy()
print(x is y)
y['a'] = 99
print(x)

import copy
x = {'a': {'python': '2.7'}, 'b': {'python': '3.6'}}
y = copy.deepcopy(x)
y['a']['python'] = '2.7.15'
print(x)
print(y)