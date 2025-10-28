def binary_search(arr, key, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == key:
            return mid + 1
        elif arr[mid] < key:
            start = mid + 1
        else:
            end = mid - 1
    return start

def binary_insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        # Find correct position in sorted part arr[0...i-1]
        pos = binary_search(arr, key, 0, i - 1)

        # Shift elements to make room for the key
        arr[pos+1:i+1] = arr[pos:i]
        arr[pos] = key

# Example usage
arr = [37, 23, 0, 17, 12, 72, 31]
binary_insertion_sort(arr)
print("Binary Insertion Sort:", arr)
