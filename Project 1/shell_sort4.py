def sequence4(max_val, gaps: list[int]):
    i = 0
    while 4 ** (i + 1) + 3 * 2 ** i + 1 < max_val:
        gaps.append(4 ** (i + 1) + 3 * 2 ** i + 1)
        i += 1
    gaps.append(1)
    gaps.sort(reverse = True)
    


def shell_sort4(nums: list[int]):
    gaps = []
    sequence4(len(nums), gaps)
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