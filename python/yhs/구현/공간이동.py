'''이코테'''

n = int(input())
x,y = 1,1
plans = input().split()

dy = [0,0,-1,1]
dx = [1,-1,0,0]
move_type = ['R','L','U','D']

for plan in plans:
    if plan in move_type:
        nx = x + dx[move_type.index(plan)]
        ny = y + dy[move_type.index(plan)]
    if nx <1 or ny<1 or nx>n or ny>n:
        continue
    x,y = nx, ny


print(y,x)