'''
프로그래머스 bfs
내풀이
'''
import heapq
def solution(begin, target, words):
    if target not in words:
        return 0
    else: words.remove(target)
    n = len(words) + 2
    m = len(begin)
    o = 0
    graph = [[] for _ in range(n)]
    test1 =[]
    test1.append(list(begin))
    distance = [1e9] * n
    for i in words:
        test1.append(list(i))
    test1.append(list(target))
    for a in range(n):
        for b in range(n):
            for c in range(m):
                if test1[a][c] == test1[b][c]:
                    o += 1
            if o+1 == m:
                graph[a].append(b)
            o = 0
    def dij(start):
        q = []
        heapq.heappush(q,(0,start))
        distance[start] = 0
        while q:
            dist, now = heapq.heappop(q)
            if distance[now] < dist:
                continue
            for i in graph[now]:
                cost = dist + 1
                if cost < distance[i]:
                    distance[i] = cost
                    heapq.heappush(q,(cost,i))
    dij(0)
    
    answer = distance[n-1]
    return answer



'''다른사람풀이

from collections import deque


def get_adjacent(current, words):
    for word in words:
        if len(current) != len(word):
            continue

        count = 0
        for c, w in zip(current, word):
            if c != w:
                count += 1

        if count == 1:
            yield word


def solution(begin, target, words):
    dist = {begin: 0}
    queue = deque([begin])

    while queue:
        current = queue.popleft()

        for next_word in get_adjacent(current, words):
            if next_word not in dist:
                dist[next_word] = dist[current] + 1
                queue.append(next_word)

    return dist.get(target, 0)




'''

