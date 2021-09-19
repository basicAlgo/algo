#순서가 있는 수정가능한 객체
#수정, 삭제, 추가가 가능
#list는 [] 대괄호로 작성되어지며, 내부 원소는 ,로 구분됩니다.

a = [1, 3, 5, 6]
print(type(a))
print(a[0])
print(a[3])

#IndexError: list index out of range
#print(a[4])

b = list()
print(b)
b.append(5)
b.append("123")
b.append(1.4)
print(b)

#+연산자로 list 합치는 것이 가능
a = [1,3,5]
b = [2,7]
print(a+b)

a = list("가나다")
print(a)

#list indexing
#-음수 인덱싱 값도 허용, 역순으로 인덱싱
s = 'show how to index into sequences'.split()
print(s)
print(s[-1])

#list slicing
#리스트변수[시작인덱스:종료인덱스:step]
print(s[1:4])
#음수 인덱싱도 슬라이싱에 사용할 수 있다.
print(s[1:-1])
#리스트변수[시작인덱스:]
print(s[3:])
#리스트변수[:종료인덱스]
print(s[:3])

print(s[:3]+s[3:] == s)

#모든 값을 복사하여 새로운 list를 만들기 위해서는 아래와 같이 입력
full_slice = s[:]
print(full_slice)

#슬라이스를 통해 새롭게 만든 변수와 값은 같지만, 같은 변수는 아니다
print(full_slice == s)
print(full_slice is s)

#리스트를 복사하는 방법 2가지
u = s.copy()
v = list(s)
print(u)
print(v)

#step만 사용하는 경우
print(s[::2])
#step을 활용하여 list reverse
print(s[::-1])

#list repetition
a = [5,3]
b = a*3
print(a)
print(b)

a = [[2,5]] * 3
print(a)
a[0].append(7)
print(a)

#list 관련 메소드 및 연산
# index(item): 리스트안에서 해당 item의 index번호를 리턴, 없는 경우 ValueError
a = ['서울', '인천', '대전', '제주도']
print(a.index('인천'))
#ValueError: '부산 is not in list
# print(a.index('부산'))

#count(item): 매칭되는 갯수를 리턴해줌
a = [1, 5, 5, 3, 7, 0, 1, 2]
print(a.count(5))
print(a.count(13))

#in 절로 list안에 포함되어 있는지 확인할 수 있다.
print(10 in a)
print(5 in a)
print(10 not in a)

#list 원소 추가
#append, insert, +, extend
a = [1, 2, 3, 4, 5]
a.append(6)
print(a)
a = [1,2,3]
a.insert(1,5)
print(a)

m = [2,5,7]
n = [3,5,9]
k = m+n
print(k)
k += [11,13]
print(k)

a = [1,2,3]
a.extend([4,5,6])
print(a)

#list 원소 삭제: del
a = [1,2,3,4,5,6,7]
del a[1]
print(a)

#remove
#list.remove(찾을아이템)
a = [1,2,3,4,5,6,7]
a.remove(3)
print(a)

a = [1,2,3,4,5,6,7]
del a[a.index(3)]
print(a)

#list 정렬
#reverse, 옵션 true 내림차순 정렬
a = [1,10,5,7,6]
a.reverse()
print(a)
a.sort()
print(a)
a = [1,10,5,7,6]
a.sort(reverse=True)
print(a)

m = '나는 파이썬을 잘하고 싶다'
m = m.split()
print(m)
m.sort(key=len)
print(m)

#list 정렬된 결과 반환
#정렬된 결과를 반환하는 함수는 본체를 변형하지 않는다
x = [1, 11, 2, 3]
y = sorted(x)
print(x)
print(y)

#reverse: iterable한 객체를 반환, 확인을 위해서는 list로 한번 더 변형 필요
x = [1, 11, 2, 3]
y = reversed(x)
print(x)
print(list(y))