"""
abc란? 추상 베이스 클래스이다.
Base 클래스를 상속받는 파생 클래스가 반드시 base 클래스의 메서드를 명시적으로 선언하여 구현하도록 강제
하는 추상화 클래스 기능이다.
"""

import abc

class BaseClass:
    _metaclass_ = abc.ABCMeta

    @abc.abstractclassmethod
    def func1(self):
        pass

    @abc.abstractclassmethod
    def func2(self):
        pass

class Tombola(abc.ABC):
    @abc.abstractclassmethod
    def load(self, iterable):
        pass

    @abc.abstractclassmethod
    def pick(self):
        pass

    def loaded(self):
        return bool(self.inspect())

    def inspect(self):
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
        self.load(items)
        return tuple(sorted(items))

"""
abc 모듈을 사용할 때는 abc.ABC 와 같이 기존 있는 라이브러리를 상속받는것이 가장 좋다.
abc 모듈은 @abstractclassmethod, @abstractstaticmethod, @abstractproperty 등이 있지만 
파이썬 3.3 이후 중단되었다.
대신 아래와 같이 사용한다.
다만 이 때 @abc.abstractmethod가 가장 안쪽 데커레이터가 되어야한다.
"""
class MyABC(abc.ABC):
    @classmethod
    @abc.abstractmethod
    def an_abstract_classmethod(cls):
        pass


import random

class BingoCage(Tombola):
    
    def __init__(self, items) -> None:
        self._randomizer = random.SystemRandom()
        self._items = []
        self.load(items)

    def load(self, items):
        self._items.extend(items)
        self._randomizer.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')
    
    def __call__(self):
        self.pick()