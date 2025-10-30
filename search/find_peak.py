# mid < mid +1
    # left = mid + 1
# mid > mid + 1
    # right = mid

def find_peak(nums):
    left = 0
    right = len(nums)-1
    while left < right:
        mid = (left+right)//2
        if nums[mid] < nums[mid +  1]:
            left = mid + 1
        else:
            right =  mid 
    return nums[left],left

print(find_peak([1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]))

