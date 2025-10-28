def merge(left, right):
    result = []
    i = j = 0

    # Compare elements from both halves
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])

    return result

def merge_sort(arr):
    # Base case: single element or empty array
    if len(arr) <= 1:
        return arr

    # Split the array into two halves
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Merge the two sorted halves
    return merge(left, right)

# Example usage
nums = [5, 3, 2, 8, 1]
print("Sorted:", merge_sort(nums))
