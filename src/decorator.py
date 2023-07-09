# 일반적으로 데레레이터는 함수를 다른 함수로 대체한다.
# 데커레이터는 모듈이 로딩될 때 바로 실행된다.
# 함수 데커레이터는 모듈이 임포트되자마자 실행되지만, 데커레이트된 함수는 호출될 때만 실행된다.
from typing import Any


def deco(func):
    def inner():
        print('running inner()')
    return inner

@deco
def target():
    print('running target()')

target()

promos = []

def promotion(promo_func):
    promos.append(promo_func)
    return promo_func

@promotion
def fidelity(order):
    return order.total() * .05 if order.customer.fidelity >= 1000 else 0

@promotion
def bulk_item(order):
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1
    return discount

@promotion
def large_order(order):
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * .07
    return 0

def best_promo(order):
    return max(promo(order) for promo in promos)

"""데커레이터를 구현하면서 프로모션 전략 함수명이 _promo 형태로 끝나지 않아도 된다.
   임시로 어떤 프로모션을 배제할 때는 데커레이터만 주석처리하면 된다.
"""

# 클로저
class Averager:

    def __init__(self) -> None:
        self.series = []

    def __call__(self, new_value: int) -> float:
        self.series.append(new_value)
        total = sum(self.series)
        return total/len(self.series)
    
# nonlocal 선언 활용
def make_averager():
    count = 0
    total = 0

    def averager(new_value):
        """
        count, total은 이 함수에서 선언한 local 변수가 아닌 nonlocal 변수이므로,
        write 수행할 수 없다. nonlocal 선언해주면 write 수행이 가능해진다.
        클로저는 간단히 말해 함수 안에 내부 함수를 구현하고 그 내부 함수를 반환하는 함수이다.
        이 때 외부함수는 자신이 가진 값 등을 내부함수에 전달하여 실행하도록 한다.

        """

        # nonlocal count, total
        count += 1
        total += new_value
        return total/count


# functools.lru_cache 데커레이터 : 재귀 알고리즘, 웹에서 정보를 가져와야하는 어플리케이션에서 유용

# 싱글 디스패치 Generic 
"""functools.singledispatch 모듈로 나왔지만, 이후에 정식으로 라이브러리로 출시되서 pip 로 설치가능하다.
   자바의 메서드 오버로딩을 파이썬에 적용하기 위해 설계된 것이 아닌, 장황하게 if/elif 블록을 가진 단일 
   함수 생성을 방지하기 위함이다.
"""
from functools import singledispatch

@singledispatch
def func(x):
    print("This is default action: ", x)

@func.register(int)
    # x가 정수인 경우 아래 코드 실행
def _(x):
    print("This is for Integer:", x)

@func.register(str)
def _(x):
    print("This is for String", x)
