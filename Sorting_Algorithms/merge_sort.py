def merge_sort(nums: list[int]):
    if len(nums) > 1:
        pivot = len(nums) // 2
        left = nums[:pivot]
        right = nums[pivot:]

        merge_sort(left)                            # Recursively sort the left half
        merge_sort(right)                           # Recursively sort the right half

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