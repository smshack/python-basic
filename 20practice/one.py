# 회문 판별 하기
# 회문은 유전자 염기서열 분석에서 많이 쓰이고
# N-gram 은 빅데이터 분석, 검색 엔진에서 많이 사용됨

# 반복문으로 문자 검사하기
word =input('단어를 입력하세요: ')

is_palindrome = True                 # 회문 판별값을 저장할 변수, 초깃값은 True
for i in range(len(word) // 2):      # 0부터 문자열 길이의 절반만큼 반복
    if word[i] != word[-1 - i]:      # 왼쪽 문자와 오른쪽 문자를 비교하여 문자가 다르면
        is_palindrome = False        # 회문이 아님
        break
 
print(is_palindrome)                 # 회문 판별값 출력


## 시퀀스 뒤집기로 문자 검사하기
print(word)
print(word[::-1])
print(word == word[::-1])    # 원래 문자열과 반대로 뒤집은 문자열을 비교

## reversed 사용 검사
print(list(word))
print(list(reversed(word)))
print(list(word) == list(reversed(word)))

## join 사용 
print(word)
print(''.join(reversed(word)))
print(word == ''.join(reversed(word)))