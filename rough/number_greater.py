from functools import reduce

# def add(x):
#     return x+2

# mylst = [2, 4, 5, 6, 7, 8, 9]
# filtered = reduce(add, mylst)
# print(filtered)

def add(x, y ):
    return x+y

list = [2, 4, 7, 3, 5]
print(reduce(add,list))