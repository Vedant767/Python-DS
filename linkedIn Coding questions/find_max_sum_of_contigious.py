#Find max sum contiguous array

def max_sum(list):
    max = 0
    sum = 0
    for i in range(len(list)):
        sum += list[i]
        if sum > max:
            max = sum
    print(f"{max}")

l1 = [1, 2, 3, 4, -10]
max_sum(l1)
# print(f"{max_sum(l1)}")