'''
프로그래머스
카카오 2018 1차 추석 트래픽 =
'''
import re
def solution(lines):
    for i in range(len(lines)):
        lines[i] = list(map(str, lines[i].split(' ')))
        lines[i].remove(lines[i][0])
        lines[i][0] = list(map(str, lines[i][0].split(':')))
        lines[i][0][1] = int(lines[i][0][1])
        lines[i][0][0] = int(lines[i][0][0])
        def sumfun(n):
            n = list(map(int,n.split('.')))
            if len(n) ==2:
                n[1] = n[1]*0.001
                n = n[0] + n[1]
            else: n = n[0]
            return n
        lines[i][1] = re.sub("s","",lines[i][1])
        lines[i][0][2]=sumfun(lines[i][0][2])
        lines[i][1]=sumfun(lines[i][1])
        lines[i][0][2] = lines[i][0][2]
        tempnum = (lines[i][0][0]*60 + lines[i][0][1])*60 + lines[i][0][2]
        lines[i][0] = [tempnum-(lines[i][1]-0.001),tempnum]
        if lines[i][0][0] < 0:
            lines[i][0][0] = 0
    cntfinal = 0
    def cal(n,m,l,o):
        for i in range(len(o)):
            if n <= o[i][0][0] <n +1 or n <= o[i][0][1] < n +1 or o[i][0][0] <= n < n+1 <=o[i][0][1]:
                m += 1
        if m >= l:
            l = m
        m = 0
        return l
    for j in range(len(lines)):
        startnum1 = lines[j][0][0]
        startnum2 = lines[j][0][1]
        tempcnt = 0
        cntfinal = max(cntfinal,cal(startnum1,tempcnt,cntfinal,lines))
        cntfinal = max(cntfinal,cal(startnum2,tempcnt,cntfinal,lines))
    # return lines
    return cntfinal

print(solution( [
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
]))