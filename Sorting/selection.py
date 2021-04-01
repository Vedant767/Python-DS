# In this sort list divided into two parts sorted and unsorted.

def selection(nums):
    for i in range(len(nums)):
        lower_index = i
        
        for j in range( i+1, len(nums)):
            if nums[lower_index] > nums[j]:
                lower_index = j

        nums[i], nums[lower_index] = nums[lower_index], nums[i]


nums = [4, 1, 2, 3, 5, 2, 1, 0, 2]
selection(nums)
print(nums)