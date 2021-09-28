'''
프로그래머스 lv1
https://programmers.co.kr/learn/courses/30/lessons/42840
'''

def solution(answers):
    a1 = [1, 2, 3, 4, 5]
    a2 = [2, 1, 2, 3, 2, 4, 2, 5]
    a3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    a1_count, a2_count, a3_count = 0, 0, 0
    for i in range(len(answers)):
        a1_index = i % 5
        a2_index = i % 8
        a3_index = i % 10

        if a1[a1_index] == answers[i]:
            a1_count += 1
        if a2[a2_index] == answers[i]:
            a2_count += 1
        if a3[a3_index] == answers[i]:
            a3_count += 1

    max_val = max(a1_count, a2_count, a3_count)
    answer = []

    if max_val == a1_count:
        answer.append(1)
    if max_val == a2_count:
        answer.append(2)
    if max_val == a3_count:
        answer.append(3)

    return answer

print(solution([1,2,3,4,5]))

# enumerate를 이용한 풀기

def solution2(answers):
    pattern1 = [1, 2, 3, 4, 5]
    pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    count = [0,0,0]
    result = []

    for i, v in enumerate(answers):
        if v == pattern1[i % (len(pattern1))]:
            count[0] += 1
        if v == pattern2[i % (len(pattern2))]:
            count[1] += 1
        if v == pattern3[i % (len(pattern3))]:
            count[2] += 1

    for i, v in enumerate(count):
        if v == max(count):
            result.append(i+1)

    return result

print(solution2([1,3,2,4,2]))