'''
내가 푼 풀이
'''
def solution(numbers):
    answer = 0
    for i in numbers:
        answer += i
    print(answer)
    if answer == 45:
        answer = 0
    else:
        answer = 45 - answer
    return answer

print(solution([1,2,3,4,6,7,8,0]))

'''
다른 사람이 푼 풀이
'''

def solution1(numbers):
    answer = 0
    check = [0] * 10
    for i in numbers:
        check[i] += 1
    for i in check:
        if i == 0:
            answer += check.index(i)
            check[check.index(i)] = 1
    return answer

print(solution1([1,2,3,4,6,7,8,0]))
