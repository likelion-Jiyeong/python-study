# 집합형 SET
test = {1,1,1,2,2,3,4,5,'a'}

test2 = {'a', 'a', 'b', 'c'}

# 두 집합간의 교집합인 데이터 개수 반환
found = len(test & test2)
print(found)


