def bubble_sort(nums):
    
    swapped = True
    
    while swapped:
        swapped = False
        
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1] :
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                
                swapped = True


nums = [21, 5, 17, 28, 24, 3, 13, 18]
bubble_sort(nums)
print(nums)