def num_max(nums, compare):

    max = nums[0]

    for num in nums[1:]:
        max = compare(max, num)
    
    return max

nums = [1, 2, 3]

comp = lambda x, y: x if x > y else y

max_num = num_max(nums, comp)
