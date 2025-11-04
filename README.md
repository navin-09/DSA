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

# dfs -> stack , bfs -> queue

| Pattern         | Data structure | Traversal type | Example problem                        |
| --------------- | -------------- | -------------- | -------------------------------------- |
| Recursion / DFS | Stack          | Deep first     | Maze solver, permutations              |
| Iterative BFS   | Queue          | Level first    | Minimum steps in a grid, shortest path |

# Greedy
🧩 1. What is a Greedy Algorithm?

A Greedy algorithm builds up a solution piece by piece, always choosing the option that looks best at the moment, hoping that this local choice leads to the global optimum.

In short:

“Pick the best available choice right now — don’t reconsider later.”

✅ Example

Coin Change (Greedy version):
If coins are [1, 5, 10, 25] and you need 63¢, take as many 25s as possible, then 10s, then 5s, then 1s.

| Level     | Problem                                                              |
| --------- | -------------------------------------------------------------------- |
| 🟢 Easy   | Assign Cookies, Lemonade Change, Maximum Units on Truck              |
| 🟡 Medium | Jump Game, Gas Station, Partition Labels, Non-overlapping Intervals  |
| 🔵 Hard   | Minimum Number of Arrows to Burst Balloons, Candy, Reorganize String |


# back_track

1) Binary choice (include / exclude) — e.g., subsets, combinations (recursive choose/skip)
Use when each element has two choices: take it or skip it.
When to use: problems where decisions are binary for each position (subset, bitmask-style).

2) For-loop over choices (combinatorial generation) — e.g., combinations by starting index
Use when you choose one option out of many available alternatives at that level (and order doesn’t matter).
When to use: combinations, subsequences, choose-from-remaining items (maintains increasing indices).

3) Permutations (visited array) — order matters
Use when order matters and you must avoid reuse of elements.
When to use: permutations, arrangements where each position can be any unused item.

4) Grid/graph DFS with visited matrix — e.g., word search, maze
Use when movement is spatial and you must mark visited cells.
When to use: pathfinding, grid word search, avoid cycles.

5) Constraint-heavy problems using empties + MRV (Sudoku-like)
Collect empties first, then pick the variable with fewest options (MRV). Good for hard constraint problems.
When to use: heavy CSPs (Sudoku, scheduling), where heuristics matter.