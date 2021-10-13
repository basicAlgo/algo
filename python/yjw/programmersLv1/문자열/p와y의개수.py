'''
https://programmers.co.kr/learn/courses/30/lessons/12916
'''

from collections import Counter

def solution(s):
    letter = Counter(s.lower())
    if letter['p'] == letter['y']:
        return True
    else:
        return False

print(solution("pPoooyY"))