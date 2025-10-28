class Solution:
    def check_two_non_repeat_no(self, arr):
        res = 0
        for i in arr:
            res ^= i
        a,b =0,0
        maskBit = res & -res #  this is important step
        for i in arr:
            if i & maskBit:
                a ^= i
            else:
                b ^= i
        return a,b

        



solution = Solution()
print(solution.check_two_non_repeat_no([2,2,3,4,5,5]))