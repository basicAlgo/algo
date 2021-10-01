#딕셔너리 정렬왕
a = {}
a['a'] = 3
a['b'] =2
a['c'] = 2.5
temp = ['a','b','c']

temp.sort(key=lambda x : a[x])

print(temp)