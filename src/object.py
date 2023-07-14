# python의 객체지향
"""
1) == 연산자와 is 연산자의 차이 
동치 연산자가 객체의 값을 비교하는 반면, is 연산자는 객체의 정체성을 비교한다.

2) 튜플의 상대적 불변성
튜플 자체는 불변형이지만 참조된 항목은 변할 수 있다. 
"""
t1 = (1, 2, [30, 40])
t2 = (1, 2, [30, 40])
print(t1 == t2)
t1[-1].append(99)
print(t1)
print(t2)
print(t1 == t2)

"""
깊은 복사와 얕은 복사
"""
import copy

class Bus:
    def __init__(self, passengers=None) -> list:
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)
    
    def pick(self, name):
        self.passengers.append(name)
    
    def drop(self, name):
        self.passengers.remove(name)

    
import copy
bus1 = Bus(['Alice', 'Julia', 'Bill'])
bus2 = copy.copy(bus1)
bus3 = copy.deepcopy(bus1)

print(id(bus1), id(bus2), id(bus3))

bus1.drop('Bill')
print(bus2.passengers)

"""
매개변수는 실제 객체가 아닌 얕은 복사된 개체가 들어온다.
이때 가변형 매개변수(ex. list)가 들어오면 문제가 발생한다.
즉 가변형 매개변수는 None으로 초기화 하거나 받지 않는것이 좋다.
"""

"""
del과 가비지 컬렉션
del은 이름을 제거하는것이지, 객체를 제거하는 것이 아니다. 
사용자가 __del__()을 직접 호출해서 쓰는것은 지양해야한다.
CPython은 가비지 컬렉션에서 참조 카운트에 기반하는데 refcount가 0이 되면
알아서 __del__()을 호출하고 매모리 해제 후 객체 제거된다.
"""