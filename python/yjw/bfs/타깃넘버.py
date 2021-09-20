'''
프로그래머스 타깃넘버
https://programmers.co.kr/learn/courses/30/lessons/43165?language=python3
'''

def solution(numbers, target):
    answer = 0
    leaves = [0]
    for num in numbers:
        tmp = []
        for parent in leaves:
            tmp.append(parent + num)
            tmp.append(parent - num)
        leaves = tmp
    for leaf in leaves:
        if leaf == target:
            answer += 1
    return answer

print(solution([1,1,1,1,1], 3))