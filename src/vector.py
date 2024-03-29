from array import array
import reprlib
import math
from typing import Any


# 특별 메서드의 활용
class Vector:
    typecode = 'd'

    def __init__(self, components) -> None:
        self._components = array(self.typecode, components)

    def __iter__(self) -> array:
        return iter(self._components)
    
    def __repr__(self):
        components = reprlib.repr(self._components)
        components - components[components.find('['):-1]
        return 'Vector({})'.format(components)
    
    def __str__(self):
        return str(tuple(self))
    

"""
파이썬은 덕 타이핑을 지원하는 언어이다. 이 뜻은 본질적으로 다른 클래스라도 객체의 적합성은 실제 유형이 아니라
특정 메소드와 속성의 존재에 의해 결정된다.
ex) 오리처럼 걷고, 오리처럼 꽥꽥거리면 그것은 틀림없이 오리이다.
"""
class Duck:
    def sound(self):
        print("꽥꽥")

class Dog:
    def sound(self):
        print("멍멍")

class Fish:
    def swim(self):
        print("헤엄")

def get_sound(animal):
    animal.sound()


duck = Duck()
dog = Dog()
fish = Fish()

get_sound(duck)
get_sound(dog)
# get_sound(fish) # AttributeError

# vector를 해시상태로 만들기
from array import array
import reprlib
import math
import functools
import operator

class Vector:
    typecode = 'd'

    def __eq__(self, __o: object) -> bool:
        return tuple(self) == tuple(__o)

    def __hash__(self) -> int:
        hashes = (hash(x) for x in self._components)
        hashes = map(hash, self._conponents) # 다음과 같이 간단하게 사용할 수 있다.
        return functools.reduce(operator.xor, hashes, 0)

"""

map 활용 
map(int, list): list의 모든 요소를 int로 변환시켜줌
모든 반복가능한 객체를 활용할 수 있음

zip 활용
list(zip(range(3), 'ABC')) -> [(0, 'A'), (1, 'B'), (2, 'C')]
"""