# -------------------------
# Minimum cost to connect ropes
# (Given list of rope lengths, repeatedly join two smallest)
# -------------------------
import heapq
from typing import List


def min_cost_connect_ropes(ropes: List[int]) -> int:
    """Return minimum total cost to connect all ropes.
    Greedy: always join two smallest ropes first."""
    if not ropes:
        return 0
    # build min-heap
    heap = ropes[:]      # copy to avoid mutating input
    heapq.heapify(heap)
    total_cost = 0
    # keep combining two smallest until one rope remains
    while len(heap) > 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        cost = a + b
        total_cost += cost
        heapq.heappush(heap, cost)
    return total_cost

# -------------------------
# Tests / example usage
# -------------------------
if __name__ == "__main__":
    print("\n--- min cost examples ---")
    # Example 1:
    ropes1 = [4, 3, 2, 6]
    # Combine 2+3=5 (cost 5), heap -> [4,5,6]; then 4+5=9 (cost 9) -> [6,9]; then 6+9=15 -> total = 5+9+15=29
    print("ropes:", ropes1, "min cost:", min_cost_connect_ropes(ropes1))  # 29

    # Example 2:
    ropes2 = [1, 2, 3, 4, 5]
    print("ropes:", ropes2, "min cost:", min_cost_connect_ropes(ropes2))  # 33

    # Example 3: edge cases
    print("empty list:", min_cost_connect_ropes([]))    # 0
    print("single rope:", min_cost_connect_ropes([10])) # 0