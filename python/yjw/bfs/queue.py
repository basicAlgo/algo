from collections import deque

q = deque()

q.append(5)
q.append(2)
q.append(3)
q.append(7)
q.popleft()
print(q)
q.append(1)
q.append(4)
q.popleft()
print(q)
#다음 출력을 위해 역순으로 바꾸기
q.reverse()
print(q)