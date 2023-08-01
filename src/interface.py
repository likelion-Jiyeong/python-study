"""
덕 타이핑 다시 이해하기
"""
from random import shuffle


# 아래 shuffle은 동작한다.
l = list(range(10))
shuffle(l) #

# 아래는 에러 발생한다. 
# 아래 클래스는 불변 시퀀스 프로토콜을 구현하고 있기 때문이다.
# 가변 시퀀스는 __setitem__()도 지원해야한다.
# deck = FrenchDeck() # 임의의 클래스
# shuffle(deck) 

def set_card(deck, position, card):
    deck._cards[position] = card

# FrenchDeck.__setitem__ = set_card
# shuffle(deck)

"""
위와 같은 구현을 멍키 패칭(monkey patching)이라고 한다. 
멍키 패칭은 소스코드를 건드리지 않고 런타임에 클래스나 모듈을 변경하는 행위이다.
또한 random.shuffle() 함수는 인수의 자료형에 대해 신경쓰지 않아도 된다. 단지 받는 객체가 가변 시퀀스
프로토콜을 구현하고 있으면 된다. 이를 동적코딩 즉, 덕 타이핑이라고 한다.
"""

"""
슬라이싱의 작동 방식
"""
class MySeq:
    def __getitem__(self, index):
        cls = type(self)
        if isinstance(index, slice):
            return cls(self._components[index])
        elif isinstance(index, numbers.Integral):
            return self._components[index]
        else:
            msg = '{cls.__name__} indices must be integers'
            raise TypeError(msg.format(cls=cls))
        return index
    
"""
isinstanc()를 많이 사용한다는 것은 객체지향 설계가 잘못된것임을 나타내지만,
__getitem()__에서 슬라이스를 처리하는 경우에는 정당화될 수 있다.
"""
    

s = MySeq()
print(s[1])
print(s[1:4])

print(slice)

