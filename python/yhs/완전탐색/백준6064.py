
# 최종정답
from math import gcd
n = int(input())
sol = []
for i in range(n):
    a, b, c, d = map(int, input().split(' '))
    e = (a*b) // gcd(a,b)
    f = 0
    start = c
    if b==d:
        d = 0
    while start <= e:
        if start%b == d:
            f = 3
            sol.append(start)
        start += a
    if f==0:
        sol.append(-1)
for i in sol:
    print(i)

# 최초답안. 브루트포스
# from math import gcd
# n = int(input())
# sol = []
# for i in range(n):
#     a, b, c, d = map(int, input().split(' '))
#     e = (a*b) // gcd(a,b)
#     f = 0
#     if c == a:
#         c = 0
#     if d == b:
#         d = 0
#     for i in range(1,e+1):
#         if i%a == c and i%b == d:
#             f = i
#             sol.append(i)
#     if f == 0:
#         sol.append(-1)
#     else: 
#         f=0
#         continue
# for i in sol:
#     print(i)

# 1차 수정 - 해시사용. 이게 왜 더 런타임 긴지 모르겠음
# from math import gcd
# n = int(input())
# sol = []
# for i in range(n):
#     a, b, c, d = map(int, input().split(' '))
#     e = (a*b) // gcd(a,b)
#     f = 0
#     # if c == a:
#     #     c = 0
#     # if d == b:
#     #     d = 0
#     temp = {}
#     for i in range(0,(e//a)):
#         temp[(i*a)+c] = 2
#     for j in range(0,(e//b)):
#         if (j*b)+d in temp:
#             sol.append((j*b)+d)
#             f = j+3
#     if f == 0:
#         sol.append(-1)
#         continue
#     else: 
#         f=0
#         continue
# for i in sol:
#     print(i)

