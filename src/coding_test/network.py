from collections import deque 

# DFS 방식 구현 (재귀함수 사용)
def solution(n, computers):
    answer = 0

    visited= [False] * n
    for com in range(n):
        if visited[com] == False:
            dfs(n, computers, com, visited)
            answer += 1 # DFS로 컴퓨터들을 다 방문하고 나오면 하나의 네트워크가 된다.

    print(f"answer >> {answer}")
    return answer

def dfs(n, computers, com, visited):
    visited[com] = True
    for connect in range(n):
        if computers[com][connect] == 1 and connect != com:
            if visited[connect] == False:
                dfs(n, computers, connect, visited)



# BFS 사용
def solution(n, computers):
    answer = 0
    visited = [False for i in range(n)]
    for com in range(n):
        if visited[com] == False:
            bfs(n, computers, com, visited)
            answer += 1

    print(f"answer >> {answer}")
    return answer

def bfs(n, computers, com, visited):
    visited[com] = True
    queue = deque([com])
    
    while queue:
        com = queue.popleft() 
        visited[com] = True
        for connect in range(n):
            if connect != com and computers[com][connect] == 1:
                if visited[connect] == False:
                    queue.append(connect)    


solution(
    3, 
    [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
)