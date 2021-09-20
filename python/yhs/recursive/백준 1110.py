# 재귀 / 백준 1110 더하기 사이클 
# https://www.acmicpc.net/problem/1110
# 브론즈 1

n = int(input())
t = 0
def solution(m):
    second = m//10
    first = m%10
    m = first * 10 + (second+first)%10
    global t
    global n
    t += 1
    if m == n:
        print(t)
    else: solution(m) 

solution(n)

