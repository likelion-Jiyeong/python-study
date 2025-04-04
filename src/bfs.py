from collections import deque

def solution(n, friendships):
    answer = 0
    visited = [False for _ in range(n)]

    graph = [[] for _ in range(n)]
    for a, b in friendships:
        graph[a].append(b)
        graph[b].append(a)

    for p in range(n):
        if not visited[p]:
            bfs(p, graph, visited)
            answer += 1      

    print(f"answer >> {answer}")

    return answer 

def bfs(p, graph, visited):
    queue = deque([p])
    visited[p] = True
    print(f"visited >> {visited}")

    while queue:
        node = queue.popleft()

        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)



solution(
    5, 
    [[0, 1], [1, 2], [3, 4]]
)       