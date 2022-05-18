print('1 ---------------------------')
i = 0                     # 초기식
while i < 100:            # while 조건식
     print(f'{i}.Hello, world!')    # 반복할 코드
     i += 1                    # 변화식
print('2 ---------------------------')
i = 100                     # 초기식
while i > 0:            # while 조건식
     print(f'{i}.Hello, world!')    # 반복할 코드
     i -= 1  

print('3 ---------------------------')
count = int(input('반복할 횟수를 입력하세요: '))
 
i = 0
while i < count:     # i가 count보다 작을 때 반복
    print('Hello, world!', i)
    i += 1

print('4 ---------------------------')
import random    # random 모듈을 가져옴
print(random.random())
print(random.random())
print(random.randint(1, 6))
print(random.randint(1, 6))
dice = [1, 2, 3, 4, 5, 6]
print(random.choice(dice))
print('5 ---------------------------') 
i = 0
while i != 3:    # 3이 아닐 때 계속 반복
    i = random.randint(1, 6)    # randint를 사용하여 1과 6 사이의 난수를 생성
    print(i)

