# 람다 클로져 사용
## 람다 표현식으로 함수 만들기
- 함수를 간단하게 작성할 때 사용 다른 함수에 넣을때 주로 사용
-lambda 매개변수들: 식
- 변수에 할당하지 않고 람다 표현식 자체를 바로 호출할 수 있음

- (lambda 매개변수들: 식)(인수들)
```
lambda x: x + 10
```

# 람다 표현식과 map, filter, reduce 함수 사용하기
## 람다 표현식에 조건부 표현식 사용하기
- lambda 매개변수들: 식1 if 조건식 else 식2
- lambda 매개변수들: 식1 if 조건식1 else 식2 if 조건식2 else 식3
- filter(함수, 반복가능한객체)

# 클로저
## 변수의 사용 범위
- 전역변수, 지역변수 사용 범위 이해 필요
- global 전역변수

## 함수 안에서 함수 사용
```
def 함수이름1():
    코드
    def 함수이름2():
        코드
```

## 클로저 사용하기
- 람다는 이름이 없는 익명 함수를 뜻하고,
- 클로저는 함수를 둘러싼 환경을 유지했다가 나중에 다시 사용하는 함수