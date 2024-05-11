from insertion_sort import insertion_sort

def hybrid1(nums: list[int], hVal):
    if len(nums) > hVal:
        pivot = len(nums) // 2
        left = nums[:pivot]
        right = nums[pivot:]

        hybrid1(left, hVal)                            # Recursively sort the left half
        hybrid1(right, hVal)                           # Recursively sort the right half

        i = j = k = 0                               # Iterators for left, right, and nums

        while i < len(left) and j < len(right):     #
            if left[i] < right[j]:                  
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
            
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1
    else:
        insertion_sort(nums)   

def hybrid_sort1(nums: list[int]):
    hVal = len(nums) ** 0.2
    hybrid1(nums, hVal)