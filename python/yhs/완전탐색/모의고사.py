'''
프로그래머스 완전탐색 모의고사
https://programmers.co.kr/learn/courses/30/lessons/42840
'''

def solution(answers):
    a = [0,0,0]
    # 맞힌 개수 구하는 
    for i in range(len(answers)):
        if (i%5 == (answers[i]-1)) : 
            a[0] += 1
        if (((i%2 == 0) and answers[i] ==2) or
            ((i%8==1) and answers[i]==1) or
            ((i%8==3) and answers[i]==3) or
            ((i%8==5) and answers[i]==4) or
            ((i%8==7) and answers[i]==5)) : 
            a[1] += 1
        if (((i%10 == 0 or i%10==1) and answers[i] == 3) or
            ((i%10 == 2 or i%10==3) and answers[i] == 1) or
            ((i%10 == 4 or i%10==5) and answers[i] == 2) or
            ((i%10 == 6 or i%10==7) and answers[i] == 4) or
            ((i%10 == 8 or i%10==9) and answers[i] == 5)) : 
            a[2] += 1
    answer = []

    # 오름차순 삽입
    for i in range(1,4):
        if a[i-1] == max(a):
            answer.append(i)

    return answer