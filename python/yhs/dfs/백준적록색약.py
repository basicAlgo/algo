'''
백준 적록색약 dfs
'''
n = int(input())
testmap = []
visited =[]
for i in range(n):
    testmap.append(list(input()))
    visited.append([0 for i in range(len(testmap[i]))])
tttt =[]
def dfs(x,y):
    if x<= -1 or y<=-1 or x>=n or y>=len(testmap[x]):
        return False
    elif visited[x][y] ==1: return False
    else: return True
ans = 0
for i in range(n):
    for j in range(len(testmap[i])):
        if visited[i][j] ==1:
            continue
        else:
            visited[i][j] = 1
            tttt.append([i,j])
            while tttt:
                x,y = tttt.pop()
                if dfs(x-1,y)==True:
                    if testmap[x][y] == testmap[x-1][y]: 
                        tttt.append([x-1,y])
                        visited[x-1][y] = 1
                if dfs(x,y-1)==True:
                    if testmap[x][y] == testmap[x][y-1]: 
                        tttt.append([x,y-1])
                        visited[x][y-1] = 1
                if dfs(x+1,y)==True:
                    if testmap[x][y] == testmap[x+1][y]: 
                        tttt.append([x+1,y])
                        visited[x+1][y] = 1
                if dfs(x,y+1)==True:
                    if testmap[x][y] == testmap[x][y+1]: 
                        tttt.append([x,y+1])
                        visited[x][y+1] = 1
            ans +=1

print(ans,end=' ')
for i in range(n):
    for j in range(len(testmap[i])):
        visited[i][j] = 0
        if testmap[i][j] == 'g':
            testmap[i][j] = 'r'
ans2 = 0
for i in range(n):
    for j in range(len(testmap[i])):
        if visited[i][j] ==1:
            continue
        else:
            visited[i][j] = 1
            tttt.append([i,j])
            while tttt:
                x,y = tttt.pop()
                if dfs(x-1,y)==True:
                    if testmap[x][y] == testmap[x-1][y]: 
                        tttt.append([x-1,y])
                        visited[x-1][y] = 1
                if dfs(x,y-1)==True:
                    if testmap[x][y] == testmap[x][y-1]: 
                        tttt.append([x,y-1])
                        visited[x][y-1] = 1
                if dfs(x+1,y)==True:
                    if testmap[x][y] == testmap[x+1][y]: 
                        tttt.append([x+1,y])
                        visited[x+1][y] = 1
                if dfs(x,y+1)==True:
                    if testmap[x][y] == testmap[x][y+1]: 
                        tttt.append([x,y+1])
                        visited[x][y+1] = 1
            ans2 +=1  
print(ans2)
