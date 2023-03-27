# 딕셔너리를 생성할 수 있는 방법은 아래와 같이 많다.
a = dict(one=1, tow=2, three=3)
b = {'one':1, 'two':2, 'three':3}
c = dict(zip(['one', 'two', 'three'], [1,2,3]))
d = dict({'three':3, 'one':1, 'two':2})
e = dict([('two', 2), ('one', 1), ('three', 3)])

# 지능형 딕셔너리
DIAL_CODES = [
    (86, 'china'),
    (91, 'India'),
    (1, 'USA'),
    (62, 'Indonesia'),
    (55, 'Brazil')
]

country_code = {country: code for code, country in DIAL_CODES}
print(country_code)

country_code = {code: country.upper() for country, code in country_code.items() if code <66}
print(country_code)

my_dict = {1:'one', 2:'two'}
key = 3
my_dict.setdefault(key, []).append('one!!')
print(my_dict)
