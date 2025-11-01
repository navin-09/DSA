# Example usage
# nums = [2, 1, 5, 3, 6]

def next_smaller(nums):
    n = len(nums)
    res = [-1] * n
    stack = []  # store indices

    for i in range(n):
        while stack and nums[stack[-1]] > nums[i]:
            res[stack.pop()] = nums[i]
        stack.append(i)
    return res


def prev_smaller(nums):
    n = len(nums)
    res = [-1] * n
    stack = []  # store indices

    for i in range(n):
        while stack and nums[stack[-1]] >= nums[i]:
            stack.pop()
        if stack:
            res[i] = nums[stack[-1]]
        stack.append(i)
    return res


def next_greater(nums):
    n = len(nums)
    res = [-1] * n
    stack = []  # store indices

    for i in range(n):
        while stack and nums[stack[-1]] < nums[i]:
            res[stack.pop()] = nums[i]
        stack.append(i)
    return res


def prev_greater(nums):
    n = len(nums)
    res = [-1] * n
    stack = []  # store indices

    for i in range(n):
        while stack and nums[stack[-1]] <= nums[i]:
            stack.pop()
        if stack:
            res[i] = nums[stack[-1]]
        stack.append(i)
    return res


# Example usage
nums = [2, 1, 5, 3, 6]
print(next_smaller(nums))  # [1, -1, 3, -1, -1]
print(prev_smaller(nums))  # [-1, -1, 1, 1, 3]
print(next_greater(nums))  # [5, 5, 6, 6, -1]
print(prev_greater(nums))  # [-1, 2, -1, 5, -1]
