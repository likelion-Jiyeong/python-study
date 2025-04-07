import heapq

def dijkstra(graph, start):
    # 시작 노드에서 각 노드까지의 최단 거리
    distances = {node: float('inf') for node in graph}
    print(f"distances >> {distances}")

    distances[start] = 0 # 시작노드에서 자기자신이므로 0으로 설정
    queue = [(0, start)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_distance > distances[current_node]: # 이미 처리된 노드면 무시
            continue
        
        # 현재 노드의 모든 이웃 확인
        for neighbor, weight in graph[current_node].items():
            # 현재 노드를 거쳐서 이웃 노드로 가는 거리
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
    return distances

graph = {
    'A': {'B': 1, 'C': 2},
    'B': {'A': 1, 'E': 2, 'D': 6},
    'C': {'A': 2, 'E': 3, 'F': 8},
    'D': {'B': 6, 'E': 1},
    'E': {'B': 2, 'C': 3, 'D': 1, 'F': 7},
    'F': {'C': 8, 'E': 7}
}

print(dijkstra(graph, 'A'))