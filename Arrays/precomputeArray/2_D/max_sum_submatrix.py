def kadane_max(arr):
    """Return maximum subarray sum (non-empty) for 1D array."""
    curr_max = arr[0]
    max_arr = arr[0]
    for i in arr:
        curr_max = max(i,curr_max+i)
        max_arr = max(curr_max,max_arr)
    return max_arr

def max_sum_submatrix_only(matrix):
    """
    Return the maximum sum of any non-empty rectangular submatrix.
    Time: O(rows^2 * cols), Space: O(cols).
    """
    if not matrix or not matrix[0]:
        raise ValueError("matrix must be non-empty")

    rows, cols = len(matrix), len(matrix[0])
    max_sum = float('-inf')

    for top in range(rows):
        col_sum = [0] * cols
        for bottom in range(top, rows):
            # add current bottom row into column sums
            for j in range(cols):
                col_sum[j] += matrix[bottom][j]

            # just get max sum for this compressed 1D array
            cur_max = kadane_max(col_sum)
            
            max_sum = max(cur_max,max_sum)

    return max_sum

mat = [
    [1,  2, -1, -4, -20],
    [-8, -3, 4, 2, 1],
    [3, 8, 10, 1, 3],
    [-4, -1, 1, 7, -6]
]

print(max_sum_submatrix_only(mat))
# Output: (29, (1, 1, 3, 3))
