import random
def quick_sort(nums):
    if len(nums) <=1:return nums
    pivot = random.choice(nums)
    left = [n for n in nums if n < pivot]
    mid = [n for n in nums if n == pivot]
    right = [n for n in nums if n > pivot]

    return quick_sort(left) + mid + quick_sort(right)

def binary_search(nums, n):
    sort_nums = quick_sort(nums)
    print(sort_nums)
    left = 0
    right = len(nums) - 1
    while(left < right):
        mid = (left+right)//2
        if nums[mid] == n : return True
        if nums[mid] < n : left = mid
        if nums[mid] > n : right = mid
    
    return False

nums = [9, 3, 5, 7, 6, 2, 1, 9, 0,-1]

print(binary_search(nums, 5))

