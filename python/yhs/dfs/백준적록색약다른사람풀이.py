import sys
sys.setrecursionlimit(10**5)
n=int(input())
a=[[" "]*(n+2)]+[list(" "+input()+" ")for i in[0]*n]+[[" "]*(n+2)]
b=[i.copy()for i in a]
def cnt(s,x,y,c):
    s[x][y]=" "
    if s[x-1][y]==c:cnt(s,x-1,y,c)
    if s[x+1][y]==c:cnt(s,x+1,y,c)
    if s[x][y-1]==c:cnt(s,x,y-1,c)
    if s[x][y+1]==c:cnt(s,x,y+1,c)
c=d=0
for i in range(1,n+1):
    for j in range(1,n+1):
        if a[i][j]!=" ":
            cnt(a,i,j,a[i][j]);c+=1
for i in range(1,n+1):
    for j in range(1,n+1):
        if b[i][j]=="G":b[i][j]="R"
for i in range(1,n+1):
    for j in range(1,n+1):
        if b[i][j]!=" ":
            cnt(b,i,j,b[i][j]);d+=1
print(c,d)