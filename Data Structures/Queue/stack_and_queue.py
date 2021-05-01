from collections import deque

numbers = deque()

numbers.appendleft('a')
numbers.appendleft('b')
numbers.appendleft('b')
numbers.appendleft('d')
numbers.pop()
print(numbers)