class Solution:
    def check_i_bit_set(self, n,i):
        return n & (1<<i) != 0

solution = Solution()
print(solution.check_i_bit_set(12,3))

# 12   --> 1 1 0 0
# 1<<3  --> 1 0 0 0 

# result 1 means true
