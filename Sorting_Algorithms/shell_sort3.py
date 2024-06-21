def sequence3(max_val, gaps: list[int]):
    i = 0
    p = 0
    while 2**p <= max_val:
        q = 0
        while 2 ** p * 3 ** q <= max_val:
            gaps.append( 2 ** p * 3 ** q)
            i += 1
            q += 1
        p += 1
    gaps.sort(reverse = True)
    


def shell_sort3(nums: list[int]):
    gaps = []
    sequence3(len(nums), gaps)
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
