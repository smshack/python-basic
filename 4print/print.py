print('1 ------------------------')
print(1, 2, 3)
print('Hello', 'Python')
print('2 sep ------------------------')
print(1, 2, 3, sep=', ')
print('Hello', 'Python', sep=' ')
print(1920, 1080, sep='x')

print('3 개행 \n ------------------------')
print(1, 2, 3, sep='\n')
print(1)
print(2)
print(3)
print(1, end='')    # end에 빈 문자열을 지정하면 다음 번 출력이 바로 뒤에 오게 됨
print(2, end='')
print(3)

print(1, end=' ')    # end에 공백 한 칸 지정
print(2, end=' ')
print(3)