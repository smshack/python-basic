# 변수와 입력값 사용하기
```
변수이름 = 값
```
![3-1](../image/3-1.png)

### 변수 규칙
- 영문 문자와 숫자를 사용할 수 있습니다.
- 대소문자를 구분합니다.
- 문자부터 시작해야 하며 숫자부터 시작하면 안 됩니다.
- _(밑줄 문자)로 시작할 수 있습니다.
- 특수 문자(+, -, *, /, $, @, &, % 등)는 사용할 수 없습니다.
- 파이썬의 키워드(if, for, while, and, or 등)는 사용할 수 없습니다.

```
>>> x = 10
>>> x
10
변수 x를 만들면서 10을 할당했습니다. 파이썬 셸에서는 변수를 입력한 뒤 엔터 키를 누르면 변수에 저장된 값이 출력됩니다.

변수에는 숫자뿐만 아니라 문자열도 넣을 수 있습니다.

>>> y = 'Hello, world!'
>>> y
'Hello, world!
```

## 변수 여러 개를 한 번에 만들기
```
>>> x, y, z = 10, 20, 30
>>> x
10
>>> y
20
>>> z
30

변수 여러 개를 만들 때 값이 모두 같아도 된다면 다음과 같은 방식도 사용할 수 있습니다
>>> x = y = z = 10
>>> x
10
>>> y
10
>>> z
10
```

## 두 변수릐 값 바꾸기
```
>>> x, y = 10, 20
>>> x, y = y, x
>>> x
20
>>> y
10
```

## 변수 삭제 하기
```
>>> x = 10
>>> del x
>>> x
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    x
NameError: name 'x' is not defined 
```

## 빈 변수 만들기
```
>>> x = None
>>> print(x)
None
>>> x
>>> (아무것도 출력되지 않음)

null 이랑 같은 상태라고 보면 됨
```

# 산술 연산 후 할당 연산자 사용
```
>>> a = 10
>>> a + 20
30
>>> a
10


>>> a = 10
>>> a = a + 20    # a와 20을 더한 후 결과를 다시 a에 저장
>>> a
30


>>> a = 10
>>> a += 20    # a와 20을 더한 후 결과를 다시 a에 저장
>>> a
30

```

## input 함수 사용하기
input()을 입력한 뒤 엔터 키를 누르면 다음 줄로 넘어갑니다. 이 상태에서 Hello, world!를 입력한 뒤 엔터 키를 누르세요.


```
변수 = input()

>>> input()
Hello, world! (입력)
'Hello, world!'


10 + 20의 결과가 30이 나오게 하려면 input에서 입력받은 문자열을 숫자(정수)로 만들어주어야 합니다.

변수 = int(input())
변수 = int(input('문자열'))
input_integer.py
a = int(input('첫 번째 숫자를 입력하세요: '))    # int를 사용하여 입력 값을 정수로 변환
b = int(input('두 번째 숫자를 입력하세요: '))    # int를 사용하여 입력 값을 정수로 변환
 
print(a + b)
```

## 한번에 여러개 값을 입력 받으려면
```
변수1, 변수2 = input().split()
변수1, 변수2 = input().split('기준문자열')
변수1, 변수2 = input('문자열').split()
변수1, 변수2 = input('문자열').split('기준문자열')
```

```
a, b = input('문자열 두 개를 입력하세요: ').split()    # 입력받은 값을 공백을 기준으로 분리
 
print(a)
print(b)
```

## map 을 사용하여 정수로 변환하기
a, b = map(int, input('숫자 두 개를 입력하세요: ').split())
 
print(a + b)