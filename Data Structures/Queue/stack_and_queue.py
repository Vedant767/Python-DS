from collections import deque

numbers = deque()

numbers.append(10)
numbers.append(20)

numbers.popleft()
print(numbers)