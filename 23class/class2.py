print('1 class 속성---------------------------')
class Person:
    bag = []
 
    def put_bag(self, stuff):
        self.bag.append(stuff)
 
james = Person()
james.put_bag('책')
print(james.bag)
 
maria = Person()
maria.put_bag('열쇠')
 
print(james.bag)
print(maria.bag)

print('2 인스턴스 속성---------------------------')
class Person2:
    def __init__(self):
        self.bag = []
 
    def put_bag(self, stuff):
        self.bag.append(stuff)
 
james2 = Person2()
james2.put_bag('책')
 
maria2 = Person2()
maria2.put_bag('열쇠')
 
print(james2.bag)
print(maria2.bag)

class Knight:
    __item_limit = 10    # 비공개 클래스 속성
 
    def print_item_limit(self):
        print(Knight.__item_limit)    # 클래스 안에서만 접근할 수 있음
 
 
x = Knight()
x.print_item_limit()    # 10
 
# print(Knight.__item_limit)    # 클래스 바깥에서는 접근할 수 없음
print('3 static method ---------------------------')

class Calc:
    @staticmethod
    def add(a, b):
        print(a + b)
 
    @staticmethod
    def mul(a, b):
        print(a * b)
 
Calc.add(10, 20)    # 클래스에서 바로 메서드 호출
Calc.mul(10, 20)    # 클래스에서 바로 메서드 호출
print('4 클래스 메서드 ---------------------------')
class Person3:
    count = 0    # 클래스 속성
 
    def __init__(self):
        Person3.count += 1    # 인스턴스가 만들어질 때
                             # 클래스 속성 count에 1을 더함
 
    @classmethod
    def print_count(cls):
        print('{0}명 생성되었습니다.'.format(cls.count))    # cls로 클래스 속성에 접근
 
james = Person3()
maria = Person3()
 
Person3.print_count()    # 2명 생성되었습니다.