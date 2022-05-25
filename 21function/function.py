print('1 def ---------------------------')
def hello():
     print('hihi')

hello()
def add(a, b):
    """이 함수는 a와 b를 더한 뒤 결과를 반환하는 함수입니다."""
    return a + b
 
x = add(10, 20)       # 함수를 호출해도 독스트링은 출력되지 않음
print(x)
 
print(add.__doc__)    # 함수의 __doc__로 독스트링 출력

def not_ten(a):
     if a == 10:
         return
     print(a, '입니다.', sep='')

not_ten(5)
not_ten(10)

def add_sub(a, b):
     return a + b, a - b

x, y = add_sub(10, 20)
z =add_sub(10, 20)
print(x,y)
print(z)

def mul(a, b):
    c = a * b
    return c
 
def add(a, b):
    c = a + b
    print(c)
    d = mul(a, b)
    print(d)
 
x = 10
y = 20
add(x, y)


def print_numbers(a, b, c):
     print(a)
     print(b)
     print(c)

print_numbers(10, 20, 30)
x = [10, 20, 30]
print_numbers(*x)
# print_numbers(*[10, 20])


def print_numbers(*args):
     for arg in args:
         print(arg)

print_numbers(10, 20, 30, 40)

def personal_info(name, age, address):
     print('이름: ', name)
     print('나이: ', age)
     print('주소: ', address)

personal_info('서명석',29,'판교')
personal_info(name='홍길동', age=30, address='서울시 용산구 이촌동')

def personal_info(name, age, address):
     print('이름: ', name)
     print('나이: ', age)
     print('주소: ', address)


x = {'name': '홍길동', 'age': 30, 'address': '서울시 용산구 이촌동'}
personal_info(**x)
personal_info(*x)

def personal_info(**kwargs):
     for kw, arg in kwargs.items():
         print(kw, ': ', arg, sep='')

personal_info(name='홍길동')
personal_info(name='홍길동', age=30, address='서울시 용산구 이촌동')

x = {'name': '홍길동'}
personal_info(**x)

y = {'name': '홍길동', 'age': 30, 'address': '서울시 용산구 이촌동'}

personal_info(**y)

def personal_info(**kwargs):
    if 'name' in kwargs:    # in으로 딕셔너리 안에 특정 키가 있는지 확인
        print('이름: ', kwargs['name'])
    if 'age' in kwargs:
        print('나이: ', kwargs['age'])
    if 'address' in kwargs:
        print('주소: ', kwargs['address'])

personal_info(**x)
personal_info(**y)

def personal_info(name='비공개', age=0, address='비공개'):
     print('이름: ', name)
     print('나이: ', age)
     print('주소: ', address)

personal_info(**y)


def hello(count):
    if count == 0:    # 종료 조건을 만듦. count가 0이면 다시 hello 함수를 호출하지 않고 끝냄
        return
    
    print('Hello, world!', count)
    
    count -= 1      # count를 1 감소시킨 뒤
    hello(count)    # 다시 hello에 넣음
 
hello(5)    # hello 함수 호출


def factorial(n):
    if n == 1:      # n이 1일 때
        return 1    # 1을 반환하고 재귀호출을 끝냄
    return n * factorial(n - 1)    # n과 factorial 함수에 n - 1을 넣어서 반환된 값을 곱함
 
print(factorial(5))