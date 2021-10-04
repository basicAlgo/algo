import time
import bisect
from collections import deque

n = int(input())
start = time.time()
a =[]
b = deque()
c = []
def yes(p,nn):
    nnn=0
    while nnn == nn:
        if len(p) ==3 or len(p)==2:
            f = int(input())
            bisect.insort(p,f)
            c.append(p[1])
            nnn += 1
            return yes(p,nn)
        elif len(p) ==4:
            g = int(input())
            bisect.insort(p,g)
            c.append(p[2])
            p.pop()
            p.popleft()
            nnn += 1
            return yes(p,nn)
        elif len(p) == 0:
            c.append(int(input()))
            p.append(c[0])
            nnn += 1
            return yes(p,nn)
        elif len(p) ==1:
            d = int(input())
            if d>=c[0]:
                c.append(c[0])
                p.append(d)
            else:
                c.append(d)
                p.appendleft(d)
            nnn += 1
            return yes(p,nn)
        # return yes(p)
    for k in c:
        print(k)
yes(b,n)

print(b)
print(time.time()-start)
# 7
# 1
# 5
# 2
# 10
# -99
# 7
# 5
        # return yes(p)
# c.append(int(input()))
# b.append(c[0])
# d = int(input())
# if d>=c[0]:
#     c.append(c[0])
#     b.append(d)
# else:
#     c.append(d)
#     b.appendleft(d)
# e = int(input())
# bisect.insort(b,e)
# c.append(b[1])

# def yes(p):
#     if len(p) ==3:
#         f = int(input())
#         bisect.insort(p,f)
#         c.append(p[1])
#     if len(p) ==4:
#         g = int(input())
#         bisect.insort(p,g)
#         c.append(p[2])
#         p.pop()
#         p.popleft()
#     if len(p) == 0:
#         c.append(int(input()))
#         p.append(c[0])
#     if len(p) ==1:
#         d = int(input())
#         if d>=c[0]:
#             c.append(c[0])
#             p.append(d)
#         else:
#             c.append(d)
#             p.appendleft(d)
#         # return yes(p)
#     if len(p) ==2:
#         e = int(input())
#         bisect.insort(p,e)
#         c.append(p[1])
#         # return yes(p)
        


    # if len(p)
    # m = int(input())
    # bisect.insort(p,m)
    # c.append(p[1])
    # l = int(input())
    # bisect.insrot()
    # b.append(p[int((len(p)+1)/2-1)])
# for i in range(n):
#     yes(b)
# for k in c:
#     print(k)
# 7
# 1
# 5
# 2
# 10
# -99
# 7
# 5