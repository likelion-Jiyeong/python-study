# 사용자 정의 콜러블형
# 파이썬에는 다양한 콜러블형이 존재하지만, 모든 파이썬 객체가 함수처럼 동작하게 만들 수 있다.
import random
from typing import Any

class BingoCage:
    def __init__(self, items) -> None:
        self._items = list(items)
        random.shuffle(self._items)
    
    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')
            # LookupError 를 사용하면 indexError, KeyError 모두 포함시킬 수 있다.

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        return self.pick()

bingo = BingoCage(range(3))
print(bingo.pick())
print(bingo())
print(callable(bingo))


# 다양한 기준으로 정렬하기 위한 함수
from operator import itemgetter, attrgetter

students = [
    ("jane", 22, "A"),
    ("dave", 32, "B"),
    ("sally", 17, "B")
]

result = sorted(students, key=itemgetter(1))
print(f"result >> {result}")

# students 리스트의 요소가 튜플이 아닌 Student 클래스의 객체라면 attrgetter를 적용해야한다.

class Student:
    def __init__(self, name, age, grade) -> None:
        self.name = name
        self.age = age
        self.grade = grade

students = [
    Student('jane', 22, 'A'),
    Student('dan', 17, 'B'),
    Student('selly', 32, 'A')
]
result = sorted(students, key=attrgetter('age'))
print(f"result2 >> {result}")

# 기존 함수로 새로운 함수를 만들기
from functools import partial

def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i
    return result 

# 일반적인 함수 사용법
def add(*args):
    return add_mul('add', *args)

def mul(*args):
    return add_mul('mul', *args)

# partial() 를 사용하면 간결하게 짤 수 있다.
add = partial(add_mul, 'add')
mul = partial(add_mul, 'mul')
print(add(1,2,3))
print(mul(1,2,3))

# partial은 하나 이상의 인수를 
