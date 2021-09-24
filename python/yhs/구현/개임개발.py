'''이코테'''


n,m = map(int, input().split())
x, y, direction = map(int, input().split())

array = []
for i in range(n):
    array.append(list(map(int, input.split())))

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction =3

array[x][y] = 1

count =1
turn_time = 0

while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    if array[nx][ny] == 0:
        array[nx][ny] ==1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    
    if turn_time ==4:
        nx = x - dx[direction]
        ny = y - dx[direction]


        
# 망한코드 ㅜㅜ 뒤로 가기 바다 이슈를 해결못함.
