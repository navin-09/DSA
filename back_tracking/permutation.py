from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visit = [False]*len(nums)
        def generate_permutations(ans):
            if len(ans) == len(nums):
                res.append(ans)
                return
            for idx,i in enumerate(nums):
                if not visit[idx]:
                    visit[idx] = True
                    generate_permutations(ans + [i])
                    visit[idx] = False
        
        generate_permutations([])
        return res
    

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
