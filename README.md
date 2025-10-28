# DSA
(a+b) % m ==> (a%m + b%m) % m
(a-b) % m ==> (a%m - b%m) % m
(a*b) % m ==> (a%m * b%m) % m

| Problem Type               | Formula               | Notes                   |
| -------------------------- | --------------------- | ----------------------- |
| Arrange r from n           | nPr = n! / (n-r)!     | Order matters           |
| Choose r from n            | nCr = n! / (r!(n-r)!) | Order doesn’t           |
| With repetition            | n^r                   | Each choice independent |
| Circular                   | (n-1)!                | Rotation same           |
| Identical objects          | n! / (p!q!r!...)      | Divide by repeats       |
| Distribute identical items | C(r+n-1, n-1)         | Stars and bars          |


# recursion
def function(parameter):
    if base_condition:          # 🛑 stopping condition
        return result
    smaller_result = function(smaller_parameter)  # 🔁 recursive call solve subproblem
    return combine(smaller_result)

# towers of hanoi.
Move all disks from A → C,
following these 3 rules:

Move only one disk at a time

A larger disk can’t be placed on a smaller one

Only the top disk of a rod can be moved

# sortings

| Concept           | Meaning                                     |
| ----------------- | ------------------------------------------- |
| Stable Sort       | Keeps order of equal elements               |
| Why Important     | Enables multi-key sorting                   |
| Stable Algorithms | Merge, Insertion, Bubble, Counting, TimSort |
| Python’s sort     | ✅ Stable (TimSort)                          |

| Stable ✅                             | Unstable ❌           |
| ------------------------------------ | -------------------- |
| Bubble Sort                          | Selection Sort       |
| Insertion Sort                       | Heap Sort            |
| Merge Sort                           | Quick Sort (usually) |
| Counting Sort                        |                      |
| TimSort (Python’s built-in `sort()`) |                      |


# selection sort

| Property | Value                                        |
| -------- | -------------------------------------------- |
| Type     | Comparison-based                             |
| Stable   | ❌ No                                         |
| In-place | ✅ Yes                                        |
| Time     | O(n²)                                        |
| Space    | O(1)                                         |
| Idea     | Repeatedly select minimum and place in front |
