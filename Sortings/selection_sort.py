def text_book_selection_sort(nums):
    n = len(nums)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums

def selection_sort(nums):
    n = len(nums)
    for i in range(n):
        for j in range(i,n):
            if nums[i] > nums[j]:
                nums[i],nums[j] = nums[j],nums[i]

    return nums

print(selection_sort([5, 3, 2, 8, 1]))