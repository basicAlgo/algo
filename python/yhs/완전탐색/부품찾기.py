'''
이코테 부품찾기
'''
def solution(n,nlist,m,mlist):
  for x in mlist:
      if x in nlist:
          print('yes', end=' ')
      else : print('no', end=' ')
 
n = int(input())
nlist = list(map(int,input().split()))
m = int(input())
mlist = list(map(int,input().split()))

solution(n,nlist,m,mlist)

