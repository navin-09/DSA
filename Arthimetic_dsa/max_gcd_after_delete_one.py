
from typing import List
from Arthimetic_dsa import gcd

def max_gcd_after_delete_one(arr: List[int]) -> int:
    n = len(arr)
    if n == 1:
        return 0  # after deleting the only element, no elements remain; define as 0

    # prefix_g[i] = gcd of arr[0..i]
    prefix_g = [0] * n
    prefix_g[0] = arr[0]
    for i in range(1, n):
        prefix_g[i] = gcd(prefix_g[i-1], arr[i])

    # suffix_g[i] = gcd of arr[i..n-1]
    suffix_g = [0] * n
    suffix_g[n-1] = arr[n-1]
    for i in range(n-2, -1, -1):
        suffix_g[i] = gcd(suffix_g[i+1], arr[i])

    # consider deleting each index
    best = 0
    for i in range(n):
        if i == 0:
            cur = suffix_g[1]
        elif i == n-1:
            cur = prefix_g[n-2]
        else:
            cur = gcd(prefix_g[i-1], suffix_g[i+1])
        best = max(best, cur)

    return best

# Example
print(max_gcd_after_delete_one([12, 15, 18]))  # delete 15 -> gcd(12,18)=6 -> prints 6
