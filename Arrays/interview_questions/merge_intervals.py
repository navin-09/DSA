from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        # sort by start time
        intervals.sort(key=lambda x: x[0])

        merged = [intervals[0]]
        for cur in intervals[1:]:
            last = merged[-1]
            # if current interval overlaps with last, merge them
            if cur[0] <= last[1]:
                last[1] = max(last[1], cur[1])
            else:
                merged.append(cur)

        return merged

solution = Solution()
print(solution.merge([[1,4],[3,5],[9,0],[8,7]]))