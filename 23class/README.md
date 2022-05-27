# 클래스 사용하기
- 클래스 : 객체를 표현하기 위한 문법
- 객체: 기사, 마법사, 궁수, 사제, 집 특정한개념이나 모양으로 존재하는것
    - 체력, 마나, 물리 공격력 등 클래스의 속성
    - 베기, 찌르기, 방어하기 등을 메서드라고 함

- 클래스 이름은 대문자로 시작해야 하고 메서드 작성 방법은 함수와 같고 반드시 들여쓰기를해야 함
- 메서드의 첫번째 매개변수는 반드시 self를 지정해야 함
```
class 클래스이름:
    def 메서드(self):
        코드
```
- 인스턴스 = 클래스()
- 인스턴스.메서드()

## 인스턴스 확인하기
- isinstance(인스턴스, 클래스)

## 클래스 속성 사용하기
- 속성(attribute)을 만들 때는 __init__ 메서드 안에서 self.속성에 값을 할당
- __init__ 메서드는 james = Person()처럼 클래스에 ( )(괄호)를 붙여서 인스턴스를 만들 때 호출되는 특별한 메서드
- __init__(initialize)이라는 이름 그대로 인스턴스(객체)를 초기화
```
class 클래스이름:
    def __init__(self):
        self.속성 = 값
```
```
class Person:
    def __init__(self):
        self.hello = '안녕하세요.'
 
    def greeting(self):
        print(self.hello)
 
james = Person()
james.greeting()    # 안녕하세요.
```

## self란?
- 인스턴스 자기 자신을 의미

## 클래스의 위치 인수, 키워드 인수
- 클래스로 인스턴스를 만들 때 위치 인수와 키워드 인수를 사용할 수 있음
- 위치 인수와 리스트 언패킹을 사용하려면 다음과 같이 *args를 사용하면 됨
```
class Person:
    def __init__(self, *args):
        self.name = args[0]
        self.age = args[1]
        self.address = args[2]
```
- 키워드 인수와 딕셔너리 언패킹을 사용하려면 다음과 같이 **kwargs를 사용하면 됨
```
class Person:
    def __init__(self, **kwargs):    # 키워드 인수
        self.name = kwargs['name']
        self.age = kwargs['age']
        self.address = kwargs['address']
```

## 비공개 속성 사용하기
- 비공개 속성: 클래스 바깥에서는 접근할 수 없고 클래스 안에서만 사용할 수 있는 속성
- __속성
```
class 클래스이름:
    def __init__(self, 매개변수)
        self.__속성 = 값
```
```
class Person:
    def __init__(self, name, age, address, wallet):
        self.name = name
        self.age = age
        self.address = address
        self.__wallet = wallet    # 변수 앞에 __를 붙여서 비공개 속성으로 만듦
 
maria = Person('마리아', 20, '서울시 서초구 반포동', 10000)
maria.__wallet -= 10000    # 클래스 바깥에서 비공개 속성에 접근하면 에러가 발생함
```