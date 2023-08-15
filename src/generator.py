"""
이터레이터란?
nex() 함수 호출 시 그 다음 값을 반환하는 객체이다.
"""

a = [1, 2, 3]
ia = iter(a)

# iter 함수를 사용하지 않고 이터레이터 구현
class MyIterator:
    def __init__(self, data) -> None:
        self.data = data
        self.position = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.position >= len(self.data):
            raise StopIteration
        result = self.data[self.position]
        self.position += 1
        return result
    

# 제너레이터? 이터레이터를 생성해주는 함수이다. 
def mygen():
    for i in range(1, 1000):
        result = i * i
        yield result

gen = (i * i for i in range(1, 1000))
gen = mygen()
print(next(gen))

# 제너레이터의 사용이유 : 메모리를 효율적으로 사용할 수 있다.