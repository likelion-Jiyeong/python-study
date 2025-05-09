from collections import Counter

def solution(nums: list, k: int) -> list:
    answer = []
    counter = Counter(nums)
    answer = [x[0] for x in counter.most_common(k)]
    answer.sort()
    
    print(f"answer >> {answer}")
    return answer


nums = [1,1,1,2,2,3]
k = 2
answer = solution(nums, k)