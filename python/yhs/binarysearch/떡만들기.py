'''
이코테 떡 만들기
'''

n, m = input().split()
n = int(n)
m = int(m)

dduklist = list(map(int, input().split()))

def makedduk(start,end):
    total = 0
    cut = (start + end) // 2
    for x in dduklist:
        if x > cut:
            total += (x-cut)
    global m
    if total == m:
        return cut
    elif total < m:
         if cut+1 == end:
             return cut
         else:
             return makedduk(start,cut)
    elif total > m : 
        if cut+1 >= end : 
            return cut
        else :
            return makedduk(cut, end)

print(makedduk(min(dduklist),max(dduklist)))

    