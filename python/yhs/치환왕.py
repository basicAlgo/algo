'''
**나중에 마크다운으로 다시정리**

string.replace()메서드는 첫 번째 문자열 인수를 두 번째 문자열 인수로 바꾼 후 새 문자열을 반환합니다. 
string.replace()메소드를 사용하여 문자열에서 특정 문자를 제거하려면for 루프를 사용하여 문자열에서 반복 당 하나의 문자를 제거 할 수 있습니다.

문자를 제거하고 바꾸지 않으려는 경우 빈 문자열을 두 번째 인수로 전달합니다.
 아래 예제 코드는string.replace()메서드를 사용하여 문자열에서 문자를 제거하는 방법을 보여줍니다.
'''
string = "Hey! What's up?"
characters = "'!?"

for x in range(len(characters)):
    string = string.replace(characters[x],"")

print(string)

#output: Hey Whats up (',!,? 3개의 특수문제 삭제)

'''
string.join(iterable)메소드는iterable 객체의 각 요소를string과 결합하고 새 문자열을 반환합니다. 
string.join()메소드를 사용하여 문자열에서 특정 문자를 제거하려면 전체 문자열을 반복하고 문자열에서 제거해야하는 문자를 삭제해야합니다.
 아래 예제 코드는string.join()을 사용하여 파이썬에서 어떻게 할 수 있는지 보여줍니다.
'''
string = "Hey! What's up?"
characters = "'!?"

string = ''.join( x for x in string if x not in characters)
print(string)

# re.sub()메서드를 사용하여 Python의 문자열에서 특정 문자 제거

'''
re모듈의 re.sub(pattern, repl, string, count)메서드는 
원래 문자열에서 정규식 pattern을 repl값으로 대체 한 후 새 문자열을 반환합니다. 
count는 문자열에서pattern을 대체하려는 횟수를 의미합니다.

문자를 제거하고 교체 할 필요가 없기 때문에repl은 빈 문자열과 같습니다. 
아래 코드 예제는re.sub()메서드를 사용하여 Python에서 문자열의 문자를 대체하는 방법을 보여줍니다.
'''

import re

string = "Hey! What's up?"
string = re.sub("\!|\'|\?","",string)
print(string)

'''
regex 표현법 (정규식?)
1. '\' : 특수문자 표시 시 특수문자 앞에 사용함으로서 특수문자임을 나타냄 
2. | or 
3. 그외에 이후 추가 정리할 url : http://pythonstudy.xyz/python/article/401-%EC%A0%95%EA%B7%9C-%ED%91%9C%ED%98%84%EC%8B%9D-Regex
4. 파이썬 공식문서 1일 1정리  
'''