class Solution:
    def no_repeat_twice(self,arr):
        res = arr[0]
        for i in arr[1:]:
            res = res ^ i
        return res        

    # below function is applied for 3 but this can be used 4, 5 .. k just replace the 3 with the required number
    def no_repeat_thrice(self,nums: list[int]) -> int:
        result = 0
        for i in range(32):
            sumi = sum((num >> i)&1 for num in nums)
            if sumi%3:
                result = result | (1<<i)

        return result


solution = Solution()
print(solution.no_repeat_twice([1,1,2,3,3,4,4,5,5,6,6]))

# Example
print(solution.no_repeat_thrice([2,2,3,2]))          # -> 3
print(solution.no_repeat_thrice([-2,-2,-2,5]))       # -> 5
