import heapq
from typing import List

# -------------------------
# Basic heap operations
# -------------------------
arr = [5, 3, 8, 1, 2]
# build a min-heap in-place
heapq.heapify(arr)        # O(n)
print("heapified:", arr)  # smallest element at arr[0]

# push (insert) an element
heapq.heappush(arr, 0)    # O(log n)
print("after push 0:", arr)

# pop (remove and return smallest)
smallest = heapq.heappop(arr)  # O(log n)
print("popped smallest:", smallest)
print("heap now:", arr)

# delete an arbitrary element (e.g., remove value 8) -- two common approaches:
# 1) lazy deletion / mark-and-skip pattern (useful when many deletions) - not shown here
# 2) remove + heapify (simple, O(n))
value_to_remove = 8
try:
    arr.remove(value_to_remove)   # O(n)
    heapq.heapify(arr)            # O(n)
    print(f"removed {value_to_remove}, heapified:", arr)
except ValueError:
    print(f"{value_to_remove} not found in heap")



