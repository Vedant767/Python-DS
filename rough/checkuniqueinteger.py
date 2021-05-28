from collections import defaultdict
def print_dic(example : dict):
    for i,j in example.items():
        print(i ,":", j)

def check(nums):
    dic = defaultdict(int)
    
    for num in nums:
        if (num in dic):
            dic[num] += 1
        else:
            dic[num] = 1
    print_dic(dic)
    for values in dic.values():
        if values == 1:
            return values
    
    return None

lst = [1,2,2]
check1 = list(set(lst))
print(check1[0])
