# 파일 사용하기
파일객체 = open(파일이름, 파일모드)
파일객체.write('문자열')
파일객체.close()

## 파일 읽기
- 변수 = 파일객체.read()


## 반복문으로 문자열 여러 줄을 파일에 쓰기
```
with open('hello.txt', 'w') as file:    # hello.txt 파일을 쓰기 모드(w)로 열기
    for i in range(3):
        file.write('Hello, world! {0}\n'.format(i))
```

## 리스트에 있는 문자열 파일에 쓰기
- 파일객체.writelines(문자열리스트)

## 파일의 내용을 한쭐 씩 읽기
- 변수 = 파일객체.readline()


## 파이썬 객체를 파일에 저장하기, 가져오기
```
import pickle
 
name = 'james'
age = 17
address = '서울시 서초구 반포동'
scores = {'korean': 90, 'english': 95, 'mathematics': 85, 'science': 82}
 
with open('james.p', 'wb') as file:    # james.p 파일을 바이너리 쓰기 모드(wb)로 열기
    pickle.dump(name, file)
    pickle.dump(age, file)
    pickle.dump(address, file)
    pickle.dump(scores, file)
```