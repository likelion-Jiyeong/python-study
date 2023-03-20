# 튜플 언패킹
# ex1.
lax_coordinates = (33.9425, -118.408056)
latitude, longitude = lax_coordinates
print(latitude)
print(longitude)

# ex2.
t = (20, 8)
quotient, remainder = divmod(*t)
print(quotient)
print(remainder)

# 초과 항목을 잡기 위한 * 사용하기
a, b, *rest = range(5)
print(f"a >> {a}, b >> {b}, rest >> {rest}")

t = (1, 2, [30, 40])
# 튜플은 불변이라서 에러 발생함
# t[2] += [50, 60]

fruits = ['grape', 'raspberry', 'apple', 'banana']
print(sorted(fruits))
print(fruits)
print(sorted(fruits, key=len))

fruits.sort()
print(fruits)

