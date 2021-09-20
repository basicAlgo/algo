#반복적으로 구현한 n!
def factorial_iterative(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

print('반복적으로 구현:', factorial_iterative(5))

def factorial_recursive(n):
    if n<=1:
        return 1
    print(n, '번째 함수가', n-1, '함수 호출')
    return n * factorial_recursive(n-1)


print('재귀적으로 구현:', factorial_recursive(5))