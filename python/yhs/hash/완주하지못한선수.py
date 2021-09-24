'''프로그래머스 해시 레벨1'''

def solution(participant, completion):
    data = dict()
    for x in participant:
        data[x] = 0
    for y in participant:
        data[y] += 1
    for z in completion:
        data[z] -= 1
    for i in data:
        if data[i] != 0:
            # 리스트 형식으로 저장할 경우 완주하지 못한 선수가 여럿일 때 출력가능.
            answer = i
    
    return answer


