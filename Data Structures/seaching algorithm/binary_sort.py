def binary(list, n):
    l = 0
    u = len(list) - 1
    
    while l <= u:
        m = l + u // 2
        if list[m] == n:
            print("Number found")
            return m
        if list[m] < n:
            l = m
        else:
            u = m

l1 = [1, 2, 3, 4, 5]
n = 3
print(f"{binary(l1, n)}")