class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_left(nums,trgt):
            n = len(nums)
            left = 0
            right = n -1
            ans = -1
            while left <= right:
                mid = (left + right) // 2
                if (nums[mid] < trgt):
                    left = mid + 1
                else:
                    if (nums[mid] == trgt):
                        ans = mid
                    right = mid -1
            return ans

        def find_right(nums,trgt):
            n = len(nums)
            left = 0
            right = n-1
            ans = -1
            while left <= right:
                mid = (left + right) // 2
                if (nums[mid] > trgt):
                    right = mid - 1 
                else:
                    if (nums[mid] == trgt):
                        ans = mid
                    left = mid + 1
            return ans


        left  = find_left(nums,target)
        right = find_right(nums,target)
        return [left, right]
