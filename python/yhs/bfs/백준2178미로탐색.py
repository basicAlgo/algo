'''
bfs
'''
from collections import deque
n,m = map(int,input().split(' '))
testmap = []
for i in range(n):
    temp = list(map(int,str(input())))
    testmap.append(temp)
move = [1,-1,1,-1]
queue = deque()
queue.append((0,0))
while queue:
    x, y = queue.popleft()
    for i in range(4):
        if i < 2:
            nx = x+move[i]
            ny = y
        else: 
            ny = y + move[i]
            nx = x
        if nx<0 or ny<0 or nx>=n or ny>=m:
            continue
        if testmap[nx][ny] ==0:
            continue
        if testmap[nx][ny] ==1:
            testmap[nx][ny] = testmap[x][y] +1
            queue.append((nx,ny))

print(testmap[n-1][m-1])