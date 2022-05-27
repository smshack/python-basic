print('1 def ---------------------------')
def plus_ten(x):
     return x + 10

print(plus_ten(1))


plus_ten = lambda x: x + 10
print(plus_ten(1))


print((lambda x: x + 10)(1))

print(list(map(lambda x: x + 10, [1, 2, 3])))\

print('2 def ---------------------------')

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(map(lambda x: str(x) if x % 3 == 0 else x, a)))
print(list(map(lambda x: str(x) if x == 1 else float(x) if x == 2 else x + 10, a)))

a = [1, 2, 3, 4, 5]
b = [2, 4, 6, 8, 10]

print(list(map(lambda x, y: x * y, a, b)))

a = [8, 3, 2, 10, 15, 7, 1, 9, 0, 11]
print(list(filter(lambda x: x > 5 and x < 10, a)))

from functools import reduce

print(reduce(lambda x, y: x + y, a))

print('3 closer ---------------------------')

x = 10          # 전역 변수
def foo():
    print(x)    # 전역 변수 출력
 
foo()
print(x)        # 전역 변수 출력

print('---------------------')

x = 10          # 전역 변수
def foo():
    x = 20      # x는 foo의 지역 변수
    print(x)    # foo의 지역 변수 출력
 
foo()
print(x)        # 전역 변수 출력
print('---------------------')
x = 10          # 전역 변수
def foo():
    global x    # 전역 변수 x를 사용하겠다고 설정
    x = 20      # x는 전역 변수
    print(x)    # 전역 변수 출력
 
foo()
print(x)        # 전역 변수 출력

print('4 function in function ---------------------------')
def print_hello():
    hello = 'Hello, world!'
    def print_message():
        print(hello)
    print_message()
 
print_hello()

print('5 closer ---------------------------')

def calc():
    a = 3
    b = 5
    total = 0
    def mul_add(x):
        nonlocal total
        total = total + a * x + b
        print(total)
    return mul_add
 
c = calc()