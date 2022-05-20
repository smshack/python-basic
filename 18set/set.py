print('1 set ---------------------------')
fruits = {'strawberry', 'grape', 'orange', 'pineapple', 'cherry'}
print(fruits)
print('orange' in fruits)
print('orange' not in fruits)

a = set('apple')
print(a)

b = set(range(5))
print(b)

c = set()
print(c)
d ={}
print(type(c))
print(type(d))

print('2 할당 연산자 ---------------------------')
a = {1, 2, 3, 4}
a |= {5}
print(a)

a = {1, 2, 3, 4}
a.update({5})
print(a)

a = {1, 2, 3, 4}
a &= {0, 1, 2, 3, 4}
print(a)

a = {1, 2, 3, 4}
a -= {3}
print(a)

a = {1, 2, 3, 4}
a ^= {3, 4, 5, 6}
print(a)

print('3 부분 집합과 상위 집합 확인하기 ---------------------------')
a = {1, 2, 3, 4}
print(a <= {1, 2, 3, 4})
print(a < {1, 2, 3, 4, 5})
print(a >= {1, 2, 3, 4})
print(a > {1, 2, 3})

print(a == {1, 2, 3, 4})
print(a != {1, 2, 3})
print(a.isdisjoint({5, 6, 7, 8}))
print(a.isdisjoint({4,5}))

print('4 ---------------------------')
a = {1, 2, 3, 4}
a.add(5)
print(a)

a.remove(3)
print(a)

a.discard(2)
print(a)
a.discard(3)
print(a)

a = {1, 2, 3, 4}
a.pop()
print(a)
a.clear()
print(a)

a = {1, 2, 3, 4}
print(len(a))

print('5 ---------------------------')
a = {1, 2, 3, 4}
b = a
print(a is b)
c =  a.copy()
b.add(5)
print(a is b)
print(b is c)
print(a)
print(b)
print(c)

a = {1, 2, 3, 4}
for i in a:
     print(i)


a = {i for i in 'apple'}
print(a)

a = {i for i in 'pineapple' if i not in 'apl'}
print(a)