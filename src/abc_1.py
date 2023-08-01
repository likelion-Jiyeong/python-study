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

