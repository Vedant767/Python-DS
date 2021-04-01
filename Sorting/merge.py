def merge(a, b):
    sorted = []
    len_a, len_b = len(a), len(b)
    i = j = 0
    
    for _ in range (len_a + len_b):
        if i < len_a and j < len_b:
            if a[i] <= b[j]:
                sorted.append(a[i])
                i +=1
            else:
                sorted.append(b[j])
                j +=1
        elif i == len_a:
            sorted.append(b[j])
            j += 1
        elif j == len_b:
            sorted.append(a[i])
            i +=1
    return sorted

def merge_sort(nums):
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2
    
    a = merge_sort(nums[:mid])
    b = merge_sort(nums[mid:])
    
    return merge(a, b)

nums = [5, 4, 3, 2, 1, 19, 0]
sort = merge_sort(nums)
print(sort)