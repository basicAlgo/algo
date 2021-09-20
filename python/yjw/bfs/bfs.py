'''
bfs: 너비 우선 탐색
가까운 노드부터 탐색하는 알고리즘
큐 자료구조를 사용함

1. 탐색 시작 노드를 큐에 삽입하고 방문 처리를 한다.
2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리를 한다.
3. 2번 과정을 더이상 수행할 수 없을 때까지 반복한다.
'''
from collections import deque

#BFS 메서드 정의
def bfs(graph, start, visited):
    q = deque([start])
    #현재 노드 방문 처리
    visited[start] = True
    #큐가 빌때까지 반복
    while q:
        v = q.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

#각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
    [], #0번 노드와 연결된 곳
    [2,3,8], #1번 노드와 연결된 곳
    [1,7], #2번 노드와 연결된 곳
    [1,4,5], #3번 노드와 연결된 곳
    [3,5], #4번 노드와 연결된 곳
    [3,4], #5번 노드와 연결된 곳
    [7], #6번 노드와 연결된 곳
    [2,6,8], #7번 노드와 연결된 곳
    [1,7] #8번 노드와 연결된 곳
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

bfs(graph, 1, visited)