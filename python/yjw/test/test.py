from collections import Counter

def countLetter(words):
    counter = {}
    for letter in words:
        if letter not in counter:
            counter[letter] = 0
        counter[letter] += 1
    return counter

print(countLetter('hello world'))

def find_max(word):
    counter = Counter(word)
    max_count = -1
    for letter in counter:
        if counter[letter] > max_count:
            max_count = counter[letter]
            max_letter = letter
    return max_letter, max_count

print(find_max('hello world'))

print(Counter('hello world').most_common())
print(Counter('hello world').most_common(1))