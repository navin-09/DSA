def binary_search(arr, target):
    arr.sort()  # ensure array is sorted
    print("Sorted:", arr)

    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True, mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False, -1


# Example
nums = [9, 3, 5, 7, 6, 2, 1, 9, 0, -1]
print(binary_search(nums, 5))
