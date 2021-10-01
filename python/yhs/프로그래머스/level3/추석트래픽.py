'''
프로그래머스
카카오 2018 1차 추석 트래픽 
'''
def solution(lines):
    for i in range(len(lines)):
        lines[i] = list(map(str, lines[i].split(' ')))
        lines[i].remove(lines[i][0])
        lines[i][0] = list(map(float, lines[i][0].split(':')))
        a = (lines[i][0]*60 + lines[i][1])*60
    return lines