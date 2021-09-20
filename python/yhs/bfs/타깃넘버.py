'''
프로그래머스 타깃넘버
https://programmers.co.kr/learn/courses/30/lessons/43165?language=python3
'''

def solution(numbers, target):
    param1 = 0
    param2 = [0]
    def numcase(param1, param2):
        for j in range(len(param2)):
            param2.append(param2[j] - param1)
            param2[j] += param1
        return param2
    for i in numbers:
        numcase(i,param2)
    return param2.count(target)