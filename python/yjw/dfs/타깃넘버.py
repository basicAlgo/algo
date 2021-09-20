'''
프로그래머스 타깃넘버
https://programmers.co.kr/learn/courses/30/lessons/43165?language=python3
DFS를 이용할 땐 하나씩 비
'''

#DFS 풀이
def solution(numbers, target):
    answer = DFS(numbers, target, 0)
    return answer

def DFS(numbers, target, depth):
    answer = 0
    if depth == len(numbers):
        print(numbers)
        if sum(numbers) == target:
            return 1
        else: return 0
    else:
        answer += DFS(numbers, target, depth+1)
        numbers[depth] *= -1
        answer += DFS(numbers, target, depth+1)
        return answer

print(solution([1,1,1,1,1], 3))