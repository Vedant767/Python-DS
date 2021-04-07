l1 = [1, 2, 3, 5]
a = [str(i) for i in l1]
b = a
b.reverse()
# print(b)
res = int("".join(a))

print(res)