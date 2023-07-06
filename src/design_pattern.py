import inspect, promotions
from typing import Any
from collections import namedtuple

Customer = namedtuple('Customer', 'name fidelity')

class LineItem:

    def __init__(self, product: str, quantity: int, price: float) -> None:
        self.product = product
        self.quantity = quantity
        self.price = price
    
    def total(self):
        return self.price * self.quantity
    
class Order:
    
    def __init__(self, customer, cart, promotion=None) -> None:
        self.customer = customer
        self.cart = cart
        self.promotion = promotion

    def total(self):
        # if문이 있는 이유는 total을 n번째 호출할 경우 __total을 재계산하는 것을 방지하기 위함
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total
    
    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion(self) # self.promotion이 함수이기 때문에 (self)
        return self.total() - discount
    
    def __repr__(self) -> str:
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())
    
def fidelity_promo(order):
    return order.total() * .05 if order.customer.fidelity >= 1000 else 0

def bulk_item_promo(order):
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1
    return discount

def large_order_promo(order):
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * .07
    return 0

joe = Customer('Johe Doe', 0)
ann = Customer('Ann Smith', 1100)
cart = [LineItem('banana', 4, 5),
        LineItem('apple', 10, 1.5),
        LineItem('watermellon', 5, 5.0)]
print(Order(joe, cart, fidelity_promo))
# fidelity_promo가 함수인데 callable 형태로 호출하지 않은것은 이해가 안됨..

# promos = [globals()[name] for name in globals()
#           if name.endswith('_promo') and name != 'best_promo']
promos = [func for name, func in inspect.getmembers(promotions, inspect.isfunction)]

def best_promo(order):
    return max(promo(order) for promo in promos)


# 명령
class MacroCommand:
    
    def __init__(self, commands) -> None:
        self.commands = list(commands)

    def __call__(self) -> Any:
        for command in self.commands:
            command()

