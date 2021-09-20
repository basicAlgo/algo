import collections


def solution(participant, completion):
    d = dict()
    hashValue = 0
    for p in participant:
        d[hash(p)] = p
        hashValue += hash(p)
        print(d)
    for c in completion:
        print(hash(c))
        hashValue -= hash(c)

    return d[hashValue]



'''
collections 모듈의 Counter 클래스는 dictionary를 확장한 클래스,
데이터의 개수를 효과적으로 셀 수 있는 기능을 제공한다.
'''
def solution1(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

print(solution1(["leo", "kiki", "eden"], ["eden", "kiki"]))
