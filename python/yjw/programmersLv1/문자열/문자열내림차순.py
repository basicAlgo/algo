'''
https://programmers.co.kr/learn/courses/30/lessons/12917
'''

def solution(s):
    answer = ''
    list = []
    for letter in s:
        list.append(letter)
    # print(list)
    list.sort(reverse = True)
    answer = "".join(list)
    # print(answer)
    return answer

print(solution("Zbcdefg"))

# python list to string
a = ['a','b','c']
strA = "".join(a)
print(strA)

a = [1,2,3]
strA = "".join(str(_) for _ in a)
print(strA)

b = [2,3,4]
strB = "".join(map(str, b))
print(strB)