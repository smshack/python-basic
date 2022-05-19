from pprint import pprint
import copy             # copy 모듈을 가져옴

print('1 ---------------------------')
a = [[10, 20], [30, 40], [50, 60]]
print(a)
a = [[10, 20],
     [30, 40],
     [50, 60] ]
print(a)

print('2 --------------------------------')
a = [[10, 20], [30, 40], [50, 60]]
print(a[0][0])
print(a[1][1])
print('3 --------------------------------')
# indent는 들여쓰기 칸 수, width는 가로 폭
pprint(a, indent=4, width=20)

print('4 --------------------------------')

for x, y in a:    # 리스트의 가로 한 줄(안쪽 리스트)에서 요소 두 개를 꺼냄
    print(x, y)
print('5 --------------------------------')

for i in a:        # a에서 안쪽 리스트를 꺼냄
    for j in i:    # 안쪽 리스트에서 요소를 하나씩 꺼냄
        print(j, end=' ')
    print()

print('6 --------------------------------')
for i in range(len(a)):            # 세로 크기
    for j in range(len(a[i])):     # 가로 크기
        print(a[i][j], end=' ')
    print()

print('7 --------------------------------')

i = 0
while i < len(a):    # 반복할 때 리스트의 크기 활용(세로 크기)
    x, y = a[i]      # 요소 두 개를 한꺼번에 가져오기
    print(x, y)
    i += 1           # 인덱스를 1 증가시킴

print('8 --------------------------------')
i = 0
while i < len(a):           # 세로 크기
    j = 0
    while j < len(a[i]):    # 가로 크기
        print(a[i][j], end=' ')
        j += 1              # 가로 인덱스를 1 증가시킴
    print()
    i += 1                  # 세로 인덱스를 1 증가시킴

print('9 --------------------------------')
a = []    # 빈 리스트 생성
print(a)

for i in range(10):
    a.append(0)    # append로 요소 추가
 
print(a)
print('10 --------------------------------')
a = []    # 빈 리스트 생성
print(a)
for i in range(3):
    line = []              # 안쪽 리스트로 사용할 빈 리스트 생성
    for j in range(2):
        line.append(0)     # 안쪽 리스트에 0 추가
    a.append(line)         # 전체 리스트에 안쪽 리스트를 추가
 
print(a)
pprint(a, indent=4, width=20)

print('11 --------------------------------')
a = [[0 for j in range(2)] for i in range(3)]
print(a)

print('12 --------------------------------')
a = [3, 1, 3, 2, 5]    # 가로 크기를 저장한 리스트
b = []    # 빈 리스트 생성
 
for i in a:      # 가로 크기를 저장한 리스트로 반복
    line = []    # 안쪽 리스트로 사용할 빈 리스트 생성
    for j in range(i):    # 리스트 a에 저장된 가로 크기만큼 반복
        line.append(0)
    b.append(line)        # 리스트 b에 안쪽 리스트를 추가
 
print(b)

print('13 --------------------------------')
a = [[0] * i for i in [3, 1, 3, 2, 5]]
print(a)
pprint(a, indent=4, width=20)

print('14 --------------------------------')

students = [
    ['john', 'C', 19],
    ['maria', 'A', 25],
    ['andrew', 'B', 7]
]
 
print(sorted(students, key=lambda student: student[1]))  # 안쪽 리스트의 인덱스 1을 기준으로 정렬
print(sorted(students, key=lambda student: student[2]))  # 안쪽 리스트의 인덱스 2를 기준으로 정렬

print('15 --------------------------------')
a = [[10, 20], [30, 40]]
b = copy.deepcopy(a)    # copy.deepcopy 함수를 사용하여 깊은 복사
b[0][0] = 500
print(a)
print(b)
pprint(a, indent=4, width=20)
pprint(b, indent=4, width=20)
