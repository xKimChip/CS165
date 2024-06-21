import math

def shell_sort1(nums: list[int]):
    k = 1
    gap = int(len(nums) // 2 ** math.log2(k))
    
    while gap >= 1:
        i = gap
        while ( i < len(nums)):
            temp = nums[i]
            j = i
            while (j >= gap and nums[j - gap] > temp):
                nums[j] = nums[j - gap]
                j -= gap
            nums[j] = temp
            i += 1
        k += 1
        gap = int(len(nums) // 2 ** math.log2(k))
        
    
 
    
    