
print('1 replace ---------------------------')
s = 'Hello, world!'
print(s)
s = s.replace('world!', 'Python')
print(s)

print('2 maketrans / translate---------------------------')
table = str.maketrans('aeiou', '12345')
print('apple'.translate(table))

print('3 split ---------------------------')
fruit = 'apple pear grape pineapple orange'
print(fruit)
fruitList = fruit.split()
print(fruitList)

fruit = 'apple, pear, grape, pineapple, orange'
print(fruit)
fruitList = fruit.split(', ')
print(fruitList)

print('4 join ---------------------------')
print(' '.join(fruitList))
print('-'.join(fruitList))

print('5 upper/ lower ---------------------------')
print('python'.upper())
print('PYTHON'.lower())

print('6 lstrip/ rstrip /strip ---------------------------')
string = '   Python   '
print(string.lstrip())
print(string.rstrip())
print(string.strip())

print('7 lstrip/ rstrip /strip ---------------------------')
string = ', python.'
print(string.lstrip(',.'))
print(string.rstrip(',.'))
print(string.strip(',.'))

print('8 ljust/ rjust /center ---------------------------')
print('python'.ljust(10))
print('python'.rjust(10))
print('python'.center(10))
print( 'python'.rjust(10).upper())

print('9 zfill ---------------------------')
print('35'.zfill(4) )       # 숫자 앞에 0을 채움
print('3.5'.zfill(6))       # 숫자 앞에 0을 채움
print('hello'.zfill(10)    )# 문자열 앞에 0을 채울 수도 있음

print('10 find /rfind /index/ rindex ---------------------------')
print('apple pineapple'.find('pl'))
print('apple pineapple'.find('xy'))
print('apple pineapple'.rfind('pl'))
print('apple pineapple'.rfind('xy'))
print('apple pineapple'.index('pl'))
print('apple pineapple'.rindex('pl'))

print('11 count---------------------------')
print('apple pineapple'.count('pl'))

print('12 서식 지정자(format specifier) --------------------------')
print('I am %s.' % 'james')
print('I am %d years old.' % 20)
print('%f' % 2.3)
print( '%.2f' % 2.3)
print('%.3f' % 2.3)
print('%10s' % 'python')
print('%-10s' % 'python')
print('Today is %d %s.' % (3, 'April'))
print('Today is %d%s.' % (3, 'April'))

print('13 format method --------------------------')
print('Hello, {0}'.format('world!'))
print('Hello, {0}'.format(100))
print('Hello, {0} {2} {1}'.format('Python', 'Script', 3.6))
print( '{0} {0} {1} {1}'.format('Python', 'Script'))
print('Hello, {} {} {}'.format('Python', 'Script', 3.6))
print( 'Hello, {language} {version}'.format(language='Python', version=3.6))
language = 'Python'
version = 3.6
lan_ver = f'Hello, {language} {version}'
print(lan_ver)
print('{{ {0} }}'.format('Python'))

print('14 format sort --------------------------')
print('{0:<10}'.format('python'))
print('{0:>10}'.format('python'))
print('{:>10}'.format('python'))

print('15 format  --------------------------')
print('%03d' % 1)
print('{0:03d}'.format(35))

print('%08.2f' % 3.6)
print('{0:08.2f}'.format(150.37))

print('{0:0<10}'.format(15))    # 길이 10, 왼쪽으로 정렬하고 남는 공간은 0으로 채움
print('{0:0>10}'.format(15))    # 길이 10, 오른쪽으로 정렬하고 남는 공간은 0으로 채움