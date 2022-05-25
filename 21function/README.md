# 함수 사용하기
- 코드의 용도를 구분할 수 있음
- 코드를 재사용할 수 있음
- 실수를 줄일 수 있음
```
def 함수이름():
     코드

def 함수이름(매개변수1, 매개변수2):
    코드

def 함수이름(매개변수):
    return 반환값

def 함수이름(매개변수):
    return 반환값1, 반환값2
```

## 위치 인수를 사용하는 함수를 만들고 호출하기
```
>>> def print_numbers(a, b, c):
...     print(a)
...     print(b)
...     print(c)
...
>>> print_numbers(10, 20, 30)
10
20
30
```

## 언패킹 사용하기
- 함수(*리스트)
- 함수(*튜플)

## 가변 인수 함수 만들기
```
def 함수이름(*매개변수):
    코드

>>> def print_numbers(*args):
...     for arg in args:
...         print(arg)
...
```

## 고정 인수와 가변 인수를 함께 사용하기
```
>> def print_numbers(a, *args):
...     print(a)
...     print(args)
...
>>> print_numbers(1)
1
()
>>> print_numbers(1, 10, 20)
1
(10, 20)
>>> print_numbers(*[10, 20, 30])
10
(20, 30)
단, 이때 def print_numbers(*args, a):처럼 *args가 고정 매개변수보다 앞쪽에 오면 안 됩니다. 매개변수 순서에서 *args는 반드시 가장 뒤쪽에 와야 합니다.
```

## 키워드 인수 사용하기
```
def personal_info(name, age, address):
     print('이름: ', name)
     print('나이: ', age)
     print('주소: ', address)

personal_info('서명석',29,'판교')
함수(키워드=값)
```

## 키워드 인수와 딕셔너리 언패킹 사용
- 딕셔너리를 사용해서 키워드 인수로 값을 넣는 딕셔너리 언패킹
- 함수(**딕셔너리)
```
>>> def personal_info(name, age, address):
...     print('이름: ', name)
...     print('나이: ', age)
...     print('주소: ', address)
...
```

```
def 함수이름(**매개변수):
    코드
```

```
>>> def personal_info(**kwargs):
...     for kw, arg in kwargs.items():
...         print(kw, ': ', arg, sep='')
...
```
```
** 형식으로 사용하는 이유
딕셔너리는키- 값 쌍 형태로 값이 저장되어 있기 때문에
한번만 쓰는 경우 키만 나오고
딕셔너리를 한번에 언패킹 하면 키를사용한다는 뜻이 됨

```

## 키워드 인수를 사용하는 가변 인수 함수 만들기
```
def 함수이름(**매개변수):
    코드
```
```
>>> def personal_info(**kwargs):
...     for kw, arg in kwargs.items():
...         print(kw, ': ', arg, sep='')
...
```

## 매개변수 초기값 지정
```
def 함수이름(매개변수=값):
    코드
```

```
def personal_info(name, age, address='비공개'):
...     print('이름: ', name)
...     print('나이: ', age)
...     print('주소: ', address)
```

## 재귀호출 사용하기
- 재귀 호출은 코드가 간단한 편이지만 머릿속으로 생각을 많이 해야 함
