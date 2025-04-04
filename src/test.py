# import numpy as np


# res = [-4.8919826  -0.20179339]
# sorted_predicted_ids = np.argsort(res).tolist()[::-1]
# print(sorted_predicted_ids)



# comprehension
mylist = [3, 2, 6, 7]
result = [i*i if i%2==0 else i for i in mylist]
print(f"result >> {result}")


# 정렬
print(sorted(mylist)) # 새로운 리스트 반환
# mylist.sort() # 제자리 정렬
print(mylist)

# lambda 정렬
data_list = ['but','i','wont','hesitate','no','more','no','more','it','cannot','wait','im','yours']
data_list = list(set(data_list))
data_list.sort()
data_list.sort(key=lambda x: len(x))
print(f"data_list >> {data_list}")


# 리스트에서 가장 큰 두 수를 반환하라
# def find_max_two(arr):
#     arr.sort(reverse=True)
#     return arr[:2]

def find_max_two(arr: list[int]) -> list[int]:
    """
    정수 리스트에서 가장 큰 두 개의 값 반환
    Arguments:
        arr (list): 정수리스트
    Return:
        list (list): [가장 큰 값, 두번째로 큰 값]
    """ 
    if len(arr) < 2:
        return arr
    max1, max2 = arr[:2]
    
    if max2 > max1:
        max1, max2 = max2, max1
    for n in arr[2:]:
        if n > max1:
            max1, max2 = n, max1
        elif n > max2:
            max2 = n
    return [max1, max2]

arr = [[3, -1, 5, 0, 7, 4, 9, 1], [7]]
for a in arr:
    print(f"{a}에서 가장 큰 두 값: {find_max_two(a)}")



# 회문 판단하기
def is_palindrome(word:str) -> bool:
    """
    Arguments:
        word (str) : 검사할 키워드
    Return:
        bool : 회문이면 True, 그렇지 않으면 False 반환
    """

    if word == word[::-1]:
        return True
    else:
        return False

words = ["racecar", "rotor", "tomato", "별똥별", "코끼리"]
for word in words:
    print(f"Is '{word}' palindrome?  {is_palindrome(word)}")

import heapq

heap = []
heapq.heappush(heap, 50)
heapq.heappush(heap, 10)
heapq.heappush(heap, 100)

print(f"heap >> {heap}")

removed_value = heapq.heappop(heap)

nums = [4, 1, 7, 3, 8, 5]
heap = []

for num in nums:
    heapq.heappush(heap, (-num, num))

while heap:
    print(heapq.heappop(heap)[1])