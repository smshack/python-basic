print('1 ------------------------------')
a = (38, 21, 53, 62, 19)
print(a)

a = 38, 21, 53, 62, 19
print(a)

person = ('james', 17, 175.3, True)
print(person)
print('2 ------------------------------')
a= (38, )
print(a)
a= 38, 

print('3 ------------------------------')
a = tuple(range(10))
print(a)
b = tuple(range(5, 12))
c = tuple(range(-4, 10, 2))
print(b)
print(c)
print('4 ------------------------------')
a = [1, 2, 3]
print( tuple(a))
b = (4, 5, 6)
print(list(b))

print('5 ----------------------------------')
print(list('Hello'))
print(tuple('Hello'))
print('6 ----------------------------------')
a, b, c = [1, 2, 3]
print(a,b,c)
d, e, f = (4, 5, 6)
print(d, e, f)

print('7 ------------------------------')
x = input().split()
print(x)