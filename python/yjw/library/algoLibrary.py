from itertools import permutations, combinations, product, combinations_with_replacement
import heapq
from bisect import bisect_left, bisect_right
from collections import deque, Counter
import math
'''
코딩 테스트 시 유용한 알고리즘 모음
'''

'''
내장함수
sum(), max(), min(), sorted()
eval(): 수학 수식이 문자열 형식으로 들어오면 해당 수식을 계산한 결과를 반환한다.
'''

result = eval("(2+4)*6")
print(result)

result = sorted([9,3,2,7,4]) #오름차순 정렬
print(result)

result = sorted([9,3,2,7,4], reverse=True) #내림차순 정렬
print(result)

#리스트에 튜플이 원소로 있을 때, 이를 튜플의 두 번째 원소를 기준으로 내림차순 정렬하는 예시
result = sorted([('박성재', 27), ('김프론', 33), ('이서버', 42)], key=lambda x:x[1], reverse= True)
print(result)

'''
itertools 라이브러리
permutations: 순열
combinations: 조합
product: 중복 허용 순열
combination_with_replacement: 중복 허용 조합
'''

data = ['A','B','C']
result = list(permutations(data,3))
print(result)

result = list(combinations(data,2)) #2개를 뽑는 모든 조합 구하기
print(result)

result = list(product(data, repeat=2)) #2개를 뽑는 모든 순열 구하기(중복허용)
print(result)

result = list(combinations_with_replacement(data, 2)) #2개를 뽑는 모든 조합 구하기(중봅허용)
print(result)

'''
heapq 라이브러리
다익스트라 알고리즘을 비롯한 다양한 알고리즘에서 우선순위 큐 기능을 구현하고자 할 때 사용
최소힙으로 구성, 시간복잡도 O(NlogN)에 오름차순 정렬이 완료
힙에 원소를 삽입할 때 heap.heappush()
힙에 원소를 꺼내고자 할 때 heap.heappop()
'''

nums = [4,1,7,3,8,5]
heap = []

for num in nums:
    heapq.heappush(heap, (-num, num))

while heap:
    print(heapq.heappop(heap)[1])

'''
bisect 라이브러리
이진 탐색을 쉽게 구현할 수 있도록 해주는 라이브러리
'정렬된 배열'에서 특정한 원소를 찾아야 할 때 매우 효과적으로 사용된다.
bisect_left(), bisect_right() 함수가 가장 중요하게 사용되며, 시간 복잡도 O(logN)
bisect_left(a, x): 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 왼쪽 인덱스를 찾는 메소드
bisect_right(a, x): 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 오른쪽 인덱스를 찾는 메소드
'''

a = [1,2,4,6,8]
x = 4
print('bisect_left: ',bisect_left(a,x))
print('bisect_right: ',bisect_right(a,x))

# 활용 예시
# 값이 [left_value, right_value] 범위에 속하는 데이터의 개수를 반환하는 함수
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

a = [1,2,3,3,3,3,4,4,8,9]

#값이 4인 데이터 개수 출력
print(count_by_range(a,4,4))

#값이 [-1,3] 범위에 있는 데이터 개수 출력
print(count_by_range(a,-1,3))

'''
collections 라이브러리
deque: 스택, 큐 둘다 사용 가능
리스트의 경우 맨 뒤에 원소 추가 및 제거의 시간복잡도: O(1)
맨 앞에 원소 추가 및 제거의 시간복잡도: O(N)
맨 앞과 뒤 모두 원소를 추가하거나 제거할 때 시간복잡도: O(1)
인덱싱, 슬라이싱 기능은 없다

큐로 사용할 때: popleft()로 맨 앞 원소 제거, append(x)로 맨 뒤에 원소 x 삽입
스택으로 사용할 때: pop()로 맨 뒤 원소 제거, append(x) 로 맨 뒤에 원소 x 삽입
맨 앞에 원소 x 삽입: appendleft(x)
'''

data = deque([2,3,4])
data.appendleft(1)
data.append(5)
print(data)
print(list(data))

data.popleft()
data.pop()
print(list(data))

'''
등장 횟수를 세는 기능 제공
리스트와 같은 iterable 객체가 주어졌을 때, 해당 객체 내부의 원소가 몇 번씩 등장했는지를 알려준다.
원소별 등장 횟수를 세는 기능이 필요할 때 짧은 소스코드로 이를 구현할 수 있다.
'''

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])
print(counter['red'])
print(counter['blue'])
print(dict(counter))

'''
math 라이브러리
factorial(n): n!
sqrt(x): x의 제곱근
gcd(a,b): a와 b의 최대 공약수
pi: 상수 파이
e: 자연 상수
'''

print(math.factorial(5))
print(math.sqrt(6))
print(math.gcd(35, 14))
print(math.pi)
print(math.e)