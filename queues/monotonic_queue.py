from collections import deque
from typing import List

def sliding_window_max(nums: List[int], k: int) -> List[int]:
    if not nums or k <= 0:
        return []
    n = len(nums)
    if k == 1:
        return nums[:]  # every element is its own window

    dq = deque()   # stores indices, values in decreasing order
    res = []

    for i, val in enumerate(nums):
        # remove indices out of this window
        while dq and dq[0] <= i - k:
            dq.popleft()

        # maintain decreasing order: remove smaller values from back
        while dq and nums[dq[-1]] <= val:
            dq.pop()

        dq.append(i)

        # start adding results when first full window reached
        if i >= k - 1:
            res.append(nums[dq[0]])

    return res


def sliding_window_min(nums: List[int], k: int) -> List[int]:
    if not nums or k <= 0:
        return []
    n = len(nums)
    if k == 1:
        return nums[:]

    dq = deque()   # stores indices, values in increasing order
    res = []

    for i, val in enumerate(nums):
        while dq and dq[0] <= i - k:
            dq.popleft()

        # maintain increasing order: remove larger values from back
        while dq and nums[dq[-1]] >= val:
            dq.pop()

        dq.append(i)

        if i >= k - 1:
            res.append(nums[dq[0]])

    return res


# Quick examples
if __name__ == "__main__":
    arr = [1,3,-1,-3,5,3,6,7]
    k = 3
    print("max:", sliding_window_max(arr, k))  # [3,3,5,5,6,7]
    print("min:", sliding_window_min(arr, k))  # [-1,-3,-3,3,3,3]
