'''
내풀이 dynamic 바텀업?
'''
m = int(input())
for i in range(m):
    ans = {}
    ans[1] = [0,1]
    ans[0] = [1,0]
    nums = int(input())+1
    if nums > 1:
        for j in range(2,nums):
            ans[j] = [x+y for x,y in zip(ans[j-2],ans[j-1])]
            # ans[j] = list(map(lambda x,y:x+y,ans[j-1],ans[j-2]))
            # 해설 map(function,iterable)
            # list 에 인자 2개를 받으므로 map(lambda x,y:블라블라,x,y) 꼴이 됨.
    print(*ans[nums-1])