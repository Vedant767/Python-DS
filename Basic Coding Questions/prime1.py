def prime(num):
    list = []
    for i in range(2,num+1):
        flag = True
        for j in range(2, i):
            if i%j == 0:
                flag = False
                break
        
        if flag:
            list.append(i)    
    return list

print(prime(13))