'''
프로그래머스 그리디 체육복
https://programmers.co.kr/learn/courses/30/lessons/42862
'''

def solution(n, lost, reserve):
    stud = []
    for i in range(n):
        stud.append(1)
    for i in lost:
        stud[i-1] -= 1
    for i in reserve:
        stud[i-1] += 1
    if stud[n-1] == 0 and stud[n-2] ==2 : 
        stud[n-1] = 1
        stud[n-2] = 1
    if stud[0]== 0 and stud[1] ==2 :
        stud[0] = stud[1] = 1
    for i in range(n-2,0,-1):
        if stud[i] == 0:
            if stud[i+1] == 2: stud[i]=stud[i+1]=1
            elif stud[i-1] ==2 : stud[i]=stud[i-1]=1
            else: continue
    
    return n-stud.count(0)

    # 좋지 못한 코드. 하드코딩 많고 예외처리도 못함.