'''
String
https://programmers.co.kr/learn/courses/30/lessons/12918
'''

def solution(s):
    s = s.lower()
    if(len(s) == 4 or len(s) == 6):
        for letter in s:
            print(ord(letter) - 97)
            if ord(letter) - 97 >= 0:
                print(letter)
                return False
        return True
    else:
        return False

print(solution("A234"))