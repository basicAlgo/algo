'''
https://programmers.co.kr/learn/courses/30/lessons/81301

1478 → "one4seveneight"
234567 → "23four5six7"
10203 → "1zerotwozero3"

        s	result
"one4seveneight"	1478
"23four5six7"	234567
"2three45sixseven"	234567
"123"	123
'''
def solution(s):
    numList = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    answer = ''
    for idx, num in enumerate(numList):
        if num in s:
            s = s.replace(num, str(idx))
        answer = s
    return int(answer)

#dict를 이용한 풀이
def solution2(s):
    answer = s
    numDict = {
        'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6',
        'seven': '7', 'eight': '8', 'nine': '9'
    }
    for key, value in numDict.items():
        answer = answer.replace(key, value)
    return int(answer)

print(solution2("one4seveneight"))