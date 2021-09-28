'''다이나믹 프로그래밍
다른사람풀이

solution = lambda t, l = []: max(l) if not t else solution(t[1:], [max(x,y)+z for x,y,z in zip([0]+l, l+[0], t[0])])
'''

'''
내풀이
'''

def solution(triangle):
    t = {}
    t[1] = [(triangle[0][0] + triangle[1][0]),(triangle[0][0] + triangle[1][1])]
    for i in range(2,len(triangle)):
        t[i]=[]
        t[i].append(triangle[i][0]+t[i-1][0])
        for j in range(1,i):
            t[i].append(triangle[i][j]+max(t[i-1][j-1],t[i-1][j]))
        t[i].append(triangle[i][i]+t[i-1][i-1])

    answer = 0
    answer = max(t[len(triangle)-1])
    return answer
ㄴ