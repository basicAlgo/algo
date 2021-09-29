'''
문자열
https://www.acmicpc.net/problem/13985
'''
import re

li = input().split()
a = int(li[0])
b = int(li[2])
c = int(li[4])

if a + b == c:
    print("YES")
else:
    print("NO")

#정규 표현식을 이용한 풀이
math_expression = input()
numbers = re.findall('\d+', math_expression)
numbers = list(map(int, numbers))

if numbers[0] + numbers[1] == numbers[2]:
    print("YES")
else:
    print("NO")