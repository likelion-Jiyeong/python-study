from collections import deque

def solution(priorities, location):
    answer = 0

    queue = deque([(i, p) for i, p in enumerate(priorities)])

    while queue:
        current, priority = queue.popleft()

        if any(priority < prior for _, prior in queue):
            queue.append((current, priority))
        else:
            answer += 1 
            if current == location: # 찾고자 하는 process가 몇 번째로 수행되는지 반환
                return answer

priorities = [2, 1, 3, 2]
location = 2
answer = solution(priorities, location)
print(f"answer >> {answer}")