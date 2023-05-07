# 함수는 내장, 외장, 사용자 정의 함수로 이뤄져 있다.
# python의 매개변수
'''
1. 위치인자
처음에 나오거나 이터러블 앞에 * 기호를 붙여 전달할 수 있는 인자
2. 키워드인자
함수 호출 시 식별자가 앞에 붙은 인자 또는 ** 기호를 붙인 인자

inspect 모듈이란?
객체에 대한 정보를 얻는데 도움이 되는 몇 가지 함수를 제공
ex) 클래스의 내용을 검사하거나, 메서드의 소스 코드를 꺼내거나, 함수 인자 리스트를 추출
'''
import inspect

def test(a, b=1, *args, c = None, **kwargs):
    pass

sig = inspect.signature(test)
for param in sig.parameters.values():
    print(param.name)
    print(' - ', param.default)
    print(' - ', param.kind)

def sample(a, b=10, *args, c = None, **kwargs):
    print('a', a)
    print('b', b)
    print('c', c)
    print('args', args)
    print('kwargs', kwargs)

sample(1, 2, 3, 4, c=5, d=6, e=7)

# 함수 애너테이션
# 애너테이션은 전혀 처리하지 않으며, inspect signature에는 저장된다.
def test2(text:str, max_len: int) -> int:
    return max_len