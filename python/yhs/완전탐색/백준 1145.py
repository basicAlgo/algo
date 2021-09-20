'''
백준 1145 적어도 대부분의 배수 
https://www.acmicpc.net/problem/1145
브론즈 1
 
'''

l = list(map(int, input().split()))
n = 0
for i in range(1,1000001):
    count = 0
    for j in l:
        if i % j == 0:
            count += 1
    if count >= 3:
        n = i 
        break
    else: continue
        
print(n)

'''
재귀방식, 통과 못함,  연습해본 용도  

l = list(map(int, input().split()))
def sol(n):
    count = 0
    for i in l:
        if n % i == 0:
            count += 1
    if count >= 3:
        print(n)
    else : 
        n += 1
        sol(n)

sol(min(l))
'''
