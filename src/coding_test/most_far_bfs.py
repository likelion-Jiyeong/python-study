from collections import deque

# 리스트로 구현하기
def solution(n, edge):
    answer = 0
    # 연결된 노드 정보 그래프
    graph = [[] for _ in range(n+1)]
    print(graph)

    # 각 노드의 최단 거리 리스트
    d = [-1] * (n+1)

    # 연결된 노드 정보 추가
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])

    queue = deque([1]) # 출발노드 - 1
    d[1] = 0 # 출발노드의 최단거리를 0으로 지정


    # BFS 수행
    while queue:
        now = queue.popleft() # 현재노드

        # 현재 노드에서 이동할 수 있는 모든 노드 확인
        for i in graph[now]:
            if d[i] == -1: # 아직 방문하지 않은 노드라면
                queue.append(i)
                d[i] = d[now] + 1

    # 가장 멀리 떨어진 노드 개수 구하기
    for i in d:
        if i == max(d):
            answer += 1

    return answer

# 딕셔너리로 구현하기
def bfs(graph, n, visited):
    queue = deque([1])
    visited[1] = 1

    while queue:
        v = queue.popleft()

        for i in graph[v]:
            if visited[i] == 0:
                visited[i] = visited[v] + 1
                queue.append(i)
    return visited.count(max(visited))

def solution(n, edge):
    answer = 0
    graph = dict()
    visited = [0] * (n+1)

    for i in range(1, n+1):
        graph[i] = []
    
    for i in edge:
        graph[i[0]].append(graph[i[1]])
        graph[i[1]].append(graph[i[0]])

    return bfs(graph, n, visited)

    return answer


solution(
    6,
    [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
)