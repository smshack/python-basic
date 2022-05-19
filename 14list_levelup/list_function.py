print('1 ---------------------------')
a = [10, 20, 30]
print(a)
print(len(a))
a.append(500)
print(a)
print(len(a))

a = []
print(a)
print(len(a))
a.append(10)
print(a)
print(len(a))

a = [10, 20, 30]
print(a)
print(len(a))
a.append([500, 600])
print(a)
print(len(a))

a = [10, 20, 30]
print(a)
print(len(a))
a.extend([500, 600])
print(a)
print(len(a))


a = [10, 20, 30]
print(a)
print(len(a))
a.insert(2, 500)
print(a)
print(len(a))
a.insert(0, 400)
print(a)
print(len(a))

a.insert(len(a), 500)
print(a)
print(len(a))

a[1:1] = [800, 900]
print(a)
print(len(a))
print('2 ---------------------------')
b= a.pop()
print(b)
print(a)
print(len(a))
c= a.pop(1)
print(c)
print(a)
print(len(a))

a.remove(20)
print(a)
print(len(a))
print('3 ---------------------------')
from collections import deque    # collections 모듈에서 deque를 가져옴
a = deque([10, 20, 30])
print(list(a))
deque([10, 20, 30])
a.append(500)    # 덱의 오른쪽에 500 추가
print(list(a))
deque([10, 20, 30, 500])
a.popleft()     # 덱의 왼쪽 요소 하나 삭제
print(list(a))
deque([20, 30, 500])
print('4 ---------------------------')
a = [10, 20, 30, 15, 20, 40]
print(a.index(20))
a = [10, 20, 30, 15, 20, 40,20]
print(a.count(20))
a = [10, 20, 30, 15, 20, 40]
a.reverse()
print(a)
a = [10, 20, 30, 15, 20, 40]
a.sort()
print(a)
a = [10, 20, 30]
a.clear()
print(a)
a = [10, 20, 30]
del a[:]
print('5 ---------------------------') 
a = [10, 20, 30]
a[len(a):] = [500]
print(a)
a[len(a):] = [500, 600]
print(a)

print('6 ---------------------------') 
a = [0,0,0,0,0,0]
b = a
print(a)
print(b)
print(a is b)
b[2] = 99
print(a)
print(b)

print('7 ---------------------------') 
a = [0,0,0,0,0,0]
b = a.copy()
print(a)
print(b)
print(a is b)
b[2] = 99
print(a)
print(b)

print('8 ---------------------------') 

a = [38, 21, 53, 62, 19]
for i in a:
     print(i)

for i in [38, 21, 53, 62, 19]:
    print(i)

print('9 ---------------------------') 

a = [38, 21, 53, 62, 19]
for index, value in enumerate(a):
     print(index, value)

for index, value in enumerate(a, start=1):
     print(index, value)

print('10 ---------------------------') 

a = [38, 21, 53, 62, 19]
i = 0
while i < len(a):
     print(a[i])
     i += 1

print('11 ---------------------------')
# 리스트의 첫번째 오소를 smallest에 저장
# for로 리스트의 요소를 모두 반복 하면서 i 가 smallest 보다 작으면 smallest에 작은 값을 할당
# 리스트에서 가장 작은 값 찾기 
a = [38, 21, 53, 62, 19]
smallest = a[0]
for i in a:
     if i < smallest:
         smallest = i
print(a)
print('a에서 가장작은 값',smallest)

largest = a[0]
for i in a:
     if i > smallest:
         largest = i
print(a)
print('a에서 가장 큰 값',largest)

x = 0
for i in a:
     x += i
print('a 리스트의 합계: ',x)
print('min',min(a))
print('max',max(a))
print('sum 리스트 합계',sum(a))

print('12 ---------------------------')

a = [i for i in range(10)]        # 0부터 9까지 숫자를 생성하여 리스트 생성
print(a)
b = list(i for i in range(10))    # 0부터 9까지 숫자를 생성하여 리스트 생성
print(b)

c = [i + 5 for i in range(10)] 
print(c)

d = [i * 2 for i in range(10)]
print(d)

print('13 ---------------------------')
a = [i for i in range(10) if i % 2 == 0]    # 0~9 숫자 중 2의 배수인 숫자(짝수)로 리스트 생성
print(a)
b = [i + 5 for i in range(10) if i % 2 == 1]    # 0~9 숫자 중 홀수에 5를 더하여 리스트 생성
print(b)

print('13 ---------------------------')
a = [i * j for j in range(2, 10) for i in range(1, 10)]
print(a)
a = [i * j for j in range(2, 10)
           for i in range(1, 10)]
print(a)

print('14 ---------------------------')
a = [1.2, 2.5, 3.7, 4.6]
for i in range(len(a)):
     a[i] = int(a[i])
     print(a[i])

a = list(map(int, a))
print(a)

print('15 ---------------------------')
a = map(int,input("정수 2개 이상 입력: ").split())
print(a)
print(list(a))

x = input().split()    # input().split()의 결과는 문자열 리스트
print(x)
m = map(int, x)        # 리스트의 요소를 int로 변환, 결과는 맵 객체
print(m)
a, b = m               # 맵 객체는 변수 여러 개에 저장할 수 있음
print(a,b)
print('16 ---------------------------')
a = (38, 21, 53, 62, 19, 53)
print(a)
print(a.index(53))
print(a.count(20))

for i in a:
     print(i, end=' ')

a = tuple(i for i in range(10) if i % 2 == 0)
print(a)

a = (1.2, 2.5, 3.7, 4.6)
print(a)
a = tuple(map(int, a))
print(a)
print(min(a))
print(max(a))
print(sum(a))
