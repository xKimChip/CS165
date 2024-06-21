def hybrid(nums: list[int]):
    if len(nums) > len(nums) ** 0.2:
        pivot = len(nums) // 2
        left = nums[:pivot]
        right = nums[pivot:]

        hybrid(left)                            # Recursively sort the left half
        hybrid(right)                           # Recursively sort the right half

        i = j = k = 0                               # Iterators for left, right, and nums

        while i < len(left) and j < len(right):     
            if left[i] > right[j]:                  
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


def insertion_sort(nums: list[int]):
    for i in range(1, len(nums)):
        x = nums[i]
        j = i - 1
        while j >= 0 and x < nums[j]:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = x
