from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        visited = [False]*n
        result = []
        def dfs(path):
            if len(path) == n:
                result.append(path[:])
            for i in range(n):
                if not visited[i]:

                    visited[i] = True # back track step
                    path.append(nums[i])

                    dfs(path)

                    path.pop()
                    visited[i] = False
            

        dfs([])
        return result
    

# Test Case 1
print(Solution().permute([1, 2, 3]))
# Expected Output (order may vary):
# [
#   [1, 2, 3],
#   [1, 3, 2],
#   [2, 1, 3],
#   [2, 3, 1],
#   [3, 1, 2],
#   [3, 2, 1]
# ]

# Test Case 2
print(Solution().permute([0, 1]))
# Expected: [[0, 1], [1, 0]]

# Test Case 3
print(Solution().permute([1]))
# Expected: [[1]]

# Test Case 4 (Empty list)
print(Solution().permute([]))
# Expected: [[]]

# Test Case 5 (with duplicate elements)
print(Solution().permute([1, 1, 2]))
# Expected: will include duplicate permutations like [1,1,2], [1,2,1], etc.
