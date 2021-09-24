'''이코테'''

n = int(input())

array = []
for i in range(n):
    studata = input().split()
    array.append((studata[0],int(studata[1])))
    
print(array)
# lambda 매개변수 student 반환값 student[1] => 따라서, 각각의 튜플들을 정렬할때 [1] 값 기준으로 ㅣ정렬한다는 뜻
# key에는 함수가 들어가야함.
array = sorted(array, key=lambda student: student[1])

for stu in array[:-1]:
    print(stu[0], end='  ')

print(array[-1][0])

print(type(array))
print(type(array[0]))