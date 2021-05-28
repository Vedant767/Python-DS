def armstrong(num):
    size = len(str(num))
    sum = 0
    for i in str(num):
        sum += (int(i) ** size)
    if sum == num:
        return sum
    else:
        return False

print(armstrong(1634))