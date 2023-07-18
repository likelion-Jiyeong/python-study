"""
@classmethod와 @staticmethod
"""
class Demo:
    @classmethod
    def klassmeth(*args):
        return args
    # Demo 클래스를 무조건 첫 번째 인수로 받는다.
    
    @staticmethod
    def statmeth(*args):
        return args
    # 평범한 함수처럼 동작한다 

"""
해싱가능과 불변성
Hashable이란?
해싱이란 많은 양의 데이터를 하나의 integer와 같이 작은 양의 데이터로 변환해주는 알고리즘이다.
해시 알고리즘으로부터 얻은 hash key는 불변해야한다.
만약 해시 키가 변할 수 있으면 객체에 저장된 위치가 변하므로 빠르게 데이터를 찾을 수 없다. 
불변하는 int, string, bytes, tuple은 hashable하다. 
"""

# 해시 가능형 클래스를 만들기 위한 프로퍼티 구현
# 해시 가능형을 위해서 꼭 프로퍼티를 구현하지 않고 __hash__(), __eq__()만 제대로 구현하면 된다.

class Vector2d:
    typecode = 'd'

    def __init__(self, x, y) -> None:
        self.__x = float(x)
        self.__y = float(y)

    @property
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y
    
    def __iter__(self):
        return (i for i in (self.x, self.y))