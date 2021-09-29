from collections import Counter
'''
문자열
https://www.acmicpc.net/problem/1919
'''

a_temp = [0] * 26
b_temp = [0] * 26
count = 0
a = input()
b = input()
for i in a:
    a_temp[ord(i) - 97] += 1
for j in b:
    b_temp[ord(j) - 97] += 1
# print(a_temp)
# print(b_temp)

for i in range(26):
    if a_temp[i] or b_temp[i]:
        count += abs(a_temp[i] - b_temp[i])

print(count)

#Counter 함수를 이용한 풀이
a = Counter(input())
b = Counter(input())
count = (sum((a-b).values()) + sum((b-a).values()))

print(count)