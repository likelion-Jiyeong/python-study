"""
decorator 활용 2
decorator가 필요한 상황
"""

def register(obj, func):
    setattr(obj, func.__name__, func)

def inner():
    pass

def some_func():
    print('some func')

# inner 함수 객체에 some_func 등록

register(inner, some_func)

inner.some_func

@register(inner, some_func)
def some_func():
    print('some_func')

"""
데커레이터의 자세한 활용을 살펴보면 함수를 수정하지 않은 상태에서 추가 기능을 구현할 때 사용한다.
로그 출력 시간 측정 등에 유용한 듯하다.
"""