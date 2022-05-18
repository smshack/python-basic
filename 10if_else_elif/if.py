print('1 ---------------------------')

x = 10
if x == 10:
    print('10입니다.')
print('2 ---------------------------')

x = 15
if x >= 10:
     print('10 이상입니다.')
 
     if x == 15:
         print('15입니다.')
 
     if x == 20:
         print('20입니다.')

print('2 ---------------------------')
x = int(input('정수 하나를 입력해주세요: '))          # 입력받은 값을 변수에 저장
 
if x == 10:               # x가 10이면
    print('10입니다.')    # '10입니다.'를 출력
 
if x == 20:               # x가 20이면
    print('20입니다.')    # '20입니다.'를 출력

print('3 ---------------------------')
x = 5
if x == 10:
      print('10입니다.')
else:
      print('10이 아닙니다.')

print('4 ---------------------------') 
if True:
    print('참')    # True는 참
else:
    print('거짓')
 
if False:
    print('참')
else:
    print('거짓')    # False는 거짓
 
if None:
    print('참')
else:
    print('거짓')    # None은 거짓

print('5 ---------------------------') 

if 0:
    print('참')
else:
    print('거짓')    # 0은 거짓
 
if 1:
    print('참')    # 1은 참
else:
    print('거짓')
 
if 0x1F:    # 16진수
    print('참')    # 0x1F는 참
else:
    print('거짓')
 
if 0b1000:    # 2진수
    print('참')    # 0b1000은 참
else:
    print('거짓')
 
if 13.5:    # 실수
    print('참')    # 13.5는 참
else:
    print('거짓')

print('6 ---------------------------') 

x = 10
y = 20
 
if x == 10 and y == 20:     # x가 10이면서 y가 20일 때
    print('참')
else:
    print('거짓')

if 0 < x < 20:
    print('20보다 작은 양수입니다.')

print('7 ---------------------------') 
x = 30
 
if x == 10:             # x가 10일 때
    print('10입니다.')
elif x == 20:           # x가 20일 때
    print('20입니다.')
else:                   # 앞의 조건식에 모두 만족하지 않을 때
    print('10도 20도 아닙니다.')

print('8 ---------------------------') 
print("버튼 1번은 '콜라', 2번은 '사이다', 3번은 '환타'")
button = int(input("번호를 입력해주세요: "))
 
if button == 1:
    print('콜라')
elif button == 2:
    print('사이다')
elif button == 3:
    print('환타')
else:
    print('제공하지 않는 메뉴')