'''
내풀이
'''
# from collections import deque

# n,m,start = map(int,input().split(' '))
# temp = []
# linknode = [[]for _ in range(n+1)]
# for i in range(m):
#     temp1 = list(map(int,input().split(' ')))
#     temp.append(temp1)
#     temp1 = []
# for i in range(m):
#     linknode[temp[i][0]].append(temp[i][1])
#     linknode[temp[i][1]].append(temp[i][0])
# for i in range(n+1):
#     linknode[i].sort()
# print(linknode)
# def dfs(graph, v, visited):
#     # 현재 노드를 방문 처리
#     visited[v] = True
#     if False not in visited[1:]:
#         print(v)
#     else : print(v, end=' ')
#     # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(graph, i, visited)

# visited = [False] * (n+1)

# dfs(linknode,start,visited)

# # BFS 함수 정의
# def bfs(graph, start, visited):
#     # 큐(Queue) 구현을 위해 deque 라이브러리 사용
#     queue = deque([start])
#     # 현재 노드를 방문 처리
#     visited[start] = True
#     # 큐가 빌 때까지 반복
#     while queue:
#         # 큐에서 하나의 원소를 뽑아 출력
#         v = queue.popleft()
#         if False not in visited[1:]:
#             print(v)
#         else :print(v, end=' ')
#         # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
#         for i in graph[v]:
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i] = True

# visited = [False] * (n+1)

# bfs(linknode,start,visited)

'''
남풀이
'''
import sys

input = sys.stdin.readline
flush = sys.stdout.flush

n, m, v = map(int, input().split())
nbhd = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    nbhd[a].append(b)
    nbhd[b].append(a)

dfs = [False] * (n + 1)
S = [v]
res = []
while S:
    w = S.pop()
    if not dfs[w]:
        res.append(w)
        dfs[w] = True
        S.extend(reversed(sorted(nbhd[w])))
print(*res)
# 좋은 bfs방식 nbhd에 연결 노드들 포함
bfs = [False] * (n + 1)
bfs[v] = True
S = [v]
res = []
while S:
    res.extend(S)
    tmp = S
    S = []
    for x in tmp:
        for w in sorted(nbhd[x]):
            if not bfs[w]:
                S.append(w)
                bfs[w] = True  
print(*res)


# 정리하고 싶은거 , re, collection counter, heapq, map, filter lambda