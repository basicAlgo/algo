n, m = map(int, input().split())
array1  = list(map(int, input().split()))
array2 = list(map(int, input().split()))
array3 = []


array1.sort()
array2.sort()

for x in range(m):
    array3.append(array1[x])
    array3.append(array2[n-1-x])

array3.sort()

for x in range(m):
    array1[x], array3[-1-x] = array3[-1-x], array1[x]

result = sum(array1)

print(result)



