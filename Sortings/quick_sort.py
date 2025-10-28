
import random

def quick_sort_rec_rand(arr):
    # Base case
    if len(arr) <= 1:
        return arr

    # Choose random pivot
    pivot = random.choice(arr)

    # Partition the array
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # Recursively sort and combine
    return quick_sort_rec_rand(left) + mid + quick_sort_rec_rand(right)

# Example
print(quick_sort_rec_rand([5, 2, 1, 4, 3]))

def quick_sort_rec(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr)//2]

    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + mid + quick_sort(right)

print(quick_sort([5,2,1,4,3]))