def two_sum(nums, trgt):
    n = len(nums)
    left = 0
    right = n - 1
    pairs = []

    while left < right:
        if nums[left] + nums[right] < trgt:
            left += 1
        if nums[left] + nums[right] > trgt:
            right -= 1
        if nums[left] + nums[right] == trgt:
            pairs.append([nums[left] , nums[right]])
            left+=1
            right-=1
            # Skip duplicates
            while left < right and nums[left] == nums[left - 1]:
                left += 1
            while left < right and nums[right] == nums[right + 1]:
                right -= 1
            
    return pairs

# nums = [8, 2, 4, 5, 7, 9, 0, 6]
nums = [0, 2,2, 4, 5, 6, 7, 8, 9, 9]
print(two_sum(nums, 11))