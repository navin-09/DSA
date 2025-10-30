
def find_pivot(nums):
    left = 0
    right = len(nums) - 1
    while left < right:
        mid = (left+right)//2
        if(nums[left] < nums[mid]):
            left = mid+1
        else:
            right = mid

    return nums[left],left

def binary_search(nums, left, right,trgt):

    left = left
    right= right

    while left <= right:
        mid = (left +right) // 2
        if nums[mid] == trgt:
            return True, mid
        elif nums[mid] < trgt:
            left = mid +1
        else:
            right = mid -1
    return False, -1

def search_in_rotated_array(nums, trgt):
    pivotNumber,pivotIndex = find_pivot(nums)
    print(pivotIndex,pivotNumber)
    n = len(nums)
    left = 0 
    right = n - 1
    mid = (left+right) // 2
    if nums[mid] == trgt:
        return mid
    if trgt > nums[0]:
        return binary_search(nums,0,pivotIndex-1,trgt)
    else:
        return binary_search(nums,pivotIndex,n-1,trgt)


nums = [7, 8, 9, 0, 1, 2, 3, 4, 5, 6]
print(search_in_rotated_array(nums, 2))

