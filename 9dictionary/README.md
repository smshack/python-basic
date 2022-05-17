# 딕셔너리 사용하기
- 연관된 값을 묶어서 저장하는 용도로 딕셔너리 자료형을 제공
- 게임 캐릭터의 능력치를 딕셔너리에 저장해보면 아래와 같은 형식
```
lux = {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
```
## 딕셔너리 만들기
- 딕셔너리는 { }(중괄호) 안에 키: 값 형식으로 저장하며 각 키와 값은 ,(콤마)로 구분해줍니다.
- 딕셔너리 = {키1: 값1, 키2: 값2}
```
>>> lux = {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
>>> lux
{'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}

SyntaxError: invalid syntax: { }의 짝이 맞지 않을 때, 키:값 형식에 맞지 않을 때, 키 문자열의 ' ' 짝이 맞지 않을 때, 각 키:값을 구분할 때 ,를 넣지 않아서 발생하는 구문 에러입니다. { }, ' ' 짝이 맞는지, 키:값 형식에 맞는지, ,를 빠뜨리지 않았는지 확인해주세요.
```

## 키의 이름이 중복되면
- 가장 뒤에 넣은 값을 사용
- 중복되는 키는 저장되지 않음

## 딕셔너리 키의 자료형
-  키에는 리스트와 딕셔너리를 사용할 수 없습
- 문자열뿐만 아니라 정수, 실수, 불도 사용할 수 있음

## 빈 딕셔너리 만들기
- 딕셔너리 = {}
- 딕셔너리 = dict()

## 딕셔너리 만들기
- 딕셔너리 = dict(키1=값1, 키2=값2)
- 딕셔너리 = dict(zip([키1, 키2], [값1, 값2]))
- 딕셔너리 = dict([(키1, 값1), (키2, 값2)])
- 딕셔너리 = dict({키1: 값1, 키2: 값2})

```
>>> lux1 = dict(health=490, mana=334, melee=550, armor=18.72)    # 키=값 형식으로 딕셔너리를 만듦
>>> lux1
{'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
```
```
>>> lux2 = dict(zip(['health', 'mana', 'melee', 'armor'], [490, 334, 550, 18.72]))    # zip 함수로
>>> lux2                                                            # 키 리스트와 값 리스트를 묶음
{'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
```
```
>>> lux3 = dict([('health', 490), ('mana', 334), ('melee', 550), ('armor', 18.72)])
>>> lux3                                                  # (키, 값) 형식의 튜플로 딕셔너리를 만듦
{'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72} 
```
```
>>> lux4 = dict({'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72})     # dict 안에서
>>> lux4                                                           # 중괄호로 딕셔너리를 만듦
{'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
```

## 딕셔너리의 키에 접근하고 값 할당하기
- 딕셔너리의 키에 접근할 때는 딕셔너리 뒤에 [ ](대괄호)를 사용하며 [ ] 안에 키를 지정해주면 됨
- 딕셔너리[키]

## 딕셔너리의 키에 값 할당하기
- 딕셔너리[키] = 값
```
>>> lux = {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
>>> lux['health'] = 2037    # 키 'health'의 값을 2037로 변경
>>> lux['mana'] = 1184      # 키 'mana'의 값을 1184로 변경
>>> lux
{'health': 2037, 'mana': 1184, 'melee': 550, 'armor': 18.72}
```
```
없는 키에서 값을 가져오려 하면 
KeyError 발생
>>> lux = {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
>>> lux['attack_speed']    # lux에는 'attack_speed' 키가 없음
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    lux['attack_speed']
KeyError: 'attack_speed'
```

## 딕셔너리의 키에 값 할당하기
- 딕셔너리[키] = 값


## 딕셔너리에 키가 있는지 확인
- 키 in 딕셔너리
- 키 not in 딕셔너리
```
>>> lux = {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
>>> 'health' in lux
True
>>> 'attack_speed' in lux
False
```

## 딕셔너리의 키 개수 구하기
- len(딕셔너리)