print('1 ---------------------------')
for i in range(100):
      print(f'{i}. Hello, world!')

print('2 ---------------------------')
for i in range(5, 12):    # 5부터 11까지 반복
     print('Hello, world!', i)

print('3 ---------------------------')
for i in range(0, 10, 2):    # 0부터 8까지 2씩 증가
     print('Hello, world!', i)


print('4 ---------------------------')
for i in range(10, 0, -1):    # 10에서 1까지 1씩 감소
     print('Hello, world!', i)

for i in reversed(range(10)):    # range에 reversed를 사용하여 숫자의 순서를 반대로 뒤집음
     print('Hello, world!', i)    # 9부터 0까지 10번 반복

print('5 ---------------------------')
count = int(input('반복할 횟수를 입력하세요: '))
 
for i in range(count):
    print('Hello, world!', i)

print('6 ---------------------------')
a = [10, 20, 30, 40, 50]
for i in a:
     print(i)

fruits = ('apple', 'orange', 'grape')
for fruit in fruits:
    print(fruit)

for letter in 'Python':
    print(letter, end=' ')

for letter in reversed('Python'):
    print(letter, end=' ')