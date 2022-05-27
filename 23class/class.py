print('1 class ---------------------------')
class Person:
    def __init__(self, name, age, address):
        self.hello = '안녕하세요.'
        self.name = name
        self.age = age
        self.address = address
 
    def greeting(self):
        print('{0} 저는 {1}입니다.'.format(self.hello, self.name))
 
maria = Person('마리아', 20, '서울시 서초구 반포동')
maria.greeting()    # 안녕하세요.
print(isinstance(maria, Person))

class Person2:
    def __init__(self, *args):
        self.name = args[0]
        self.age = args[1]
        self.address = args[2]

maria2 = Person2(*['마리아', 20, '서울시 서초구 반포동'])
print(maria2.name)
print(maria2.age)
print(maria2.address)

class Person3:
    def __init__(self, **kwargs):    # 키워드 인수
        self.name = kwargs['name']
        self.age = kwargs['age']
        self.address = kwargs['address']

maria3 = Person3(name='마리아', age=20, address='서울시 서초구 반포동')
maria4 = Person3(**{'name': '마리아', 'age': 20, 'address': '서울시 서초구 반포동'})
print(maria3.name)
print(maria4.name)

class Person4:
    def __init__(self, name, age, address, wallet):
        self.name = name
        self.age = age
        self.address = address
        self.__wallet = wallet    # 변수 앞에 __를 붙여서 비공개 속성으로 만듦
 
maria5 = Person4('마리아', 20, '서울시 서초구 반포동', 10000)
# maria5.__wallet -= 10000    # 클래스 바깥에서 비공개 속성에 접근하면 에러가 발생함

class Person5:
    def __init__(self, name, age, address, wallet):
        self.name = name
        self.age = age
        self.address = address
        self.__wallet = wallet    # 변수 앞에 __를 붙여서 비공개 속성으로 만듦
 
    def pay(self, amount):
        self.__wallet -= amount   # 비공개 속성은 클래스 안의 메서드에서만 접근할 수 있음
        print('이제 {0}원 남았네요.'.format(self.__wallet))
 
maria = Person5('마리아', 20, '서울시 서초구 반포동', 10000)
maria.pay(3000)