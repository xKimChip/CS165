import math

def sequence2(max_val, gaps: list[int]):
    k = math.log2(max_val)
    i = 1
    while (i < k):
        gaps.append(2 ** i + 1)
        i += 1
    gaps.append(1)
    gaps.sort(reverse = True)

def shell_sort2(nums: list[int]):
    gaps = []
    sequence2(len(nums),gaps)
    
    for gap in gaps:
        i = gap
        while ( i < len(nums)):
            temp = nums[i]
            j = i
            while (j >= gap and nums[j - gap] > temp):
                nums[j] = nums[j - gap]
                j -= gap
            nums[j] = temp
            i += 1