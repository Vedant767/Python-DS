def insertion(nums):
    for i in range(len(nums)):
        compare = nums[i]
        
        j = i - 1
        
        while j >= 0 and compare < nums[j]:
            nums[j + 1] = nums[j]
            j -= 1
        
        nums[j + 1] = compare

nums = [5, 4, 3, 2, 1]
insertion(nums)
print(nums)