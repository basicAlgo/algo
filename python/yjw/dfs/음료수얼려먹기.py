'''
1. 특정한 지점의 주변 상, 하, 좌, 우를 살펴본 뒤에 주변 지점 중에서 값이 '0'이면서 아직
    방문하지 않은 지점이 있다면 해당 지점을 방문한다.
2. 방문한 지점에서 다시 상, 하, 좌, 우를 살펴보면서 방문을 다시 진행하면, 연결된 모든 지점을 방문 할 수 있다.
3. 1~2번의 과정을 모든 노드에 반복하며 방문하지 않은 지점의 수를 센다.
'''

#N, M을 공백으로 구분하여 입력 받기
n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# print(graph)

#dfs로 특정한 노드를 방문한 뒤 연결된 모든 노드들도 방문
def dfs(x,y):
    if x<=-1 or x >= n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

#모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)