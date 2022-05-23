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