def second_largest(nums):
    if len(nums) < 2:
        return None
    max1 = max2 = None
    for n in nums:
        if max1 is None or n > max1:
            max2 = max1
            max1 = n
        elif max2 is None or n > max2:
            max2 = n
    return max2