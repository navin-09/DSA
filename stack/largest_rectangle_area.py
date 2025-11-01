def next_smaller_index(nums):
    n = len(nums)
    res = [n] * n
    stack = []
    for i in range(n):
        while stack and nums[stack[-1]] > nums[i]:
            res[stack.pop()] = i
        stack.append(i)
    return res

def prev_smaller_index(nums):
    n = len(nums)
    res = [-1] * n
    stack = []
    for i in range(n):
        while stack and nums[stack[-1]] >= nums[i]:
            stack.pop()
        if stack:
            res[i] = stack[-1]
        stack.append(i)
    return res


def largest_rectangle_area(heights):
    n = len(heights)
    prev_sm = prev_smaller_index(heights)
    next_sm = next_smaller_index(heights)
    
    max_area = 0
    for i in range(n):
        width = next_sm[i] - prev_sm[i] - 1
        area = heights[i] * width
        max_area = max(max_area, area)
    return max_area


# Example usage
hist = [2, 1, 5, 6, 2, 3]
print(largest_rectangle_area(hist))  # Output: 10
