import bisect

# bisect란 이진 탐색을 쉽게 구현해주는 라이브러리이다.

def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
    i = bisect.bisect(breakpoints, score)
    return grades[i]

def test(n, list):
    res = bisect.bisect(list, n)
    return res

if __name__ == '__main__':

    print([grade(score) for score in [33, 99, 77, 70, 89, 90, 100]])
    print(test(5, [1,2,3,4,6,7]))