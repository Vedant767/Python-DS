a = [1, 2, 3, 4, 4]
l = set(a)
result = 0

for i in l:
    if a.count(i) == 1:
        result += i
print(result)

print(l)