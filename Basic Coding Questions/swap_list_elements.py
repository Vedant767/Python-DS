def swap(list, i, j):
    
    list[i], list[j] = list[j], list[i]
    
    return list

print(swap([1,2,3,4,5], 2,1))