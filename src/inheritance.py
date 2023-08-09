"""
다중상속 시  주의할 점
1. 인터페이스 상속과 구현 상속을 구분한다.
   다중 상속 시  상속 이유를 명확히 해야한다.
2. ABC를 이용하여 인터페이스를 명확히 한다.
3. 코드를 재사용하기 위해 믹스인을 사용한다.
4. 이름을 통해 믹스인임을 명시한다.
5. 두 개 이상의 구상 클래스에서 상속받지 않는다.   
"""
# 컴포지션의 유용한 활용
# 자식클래스가 필요한 속성만 부모클래스로부터 가져와 사용
class BixbyCal:
    def __init__(self, name, age) -> None:
        self.Robot = Robot(name, age) # Robot을 상속받지 않고 필요로한 객체를 명시적으로 가져옴

    def cal_add(self, a, b):
        return self.Robot.cal_add(a, b)
