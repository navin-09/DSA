def solveSudoku(board):
        N = 9
        digits = {str(i) for i in range(1, 10)}

        def box_index(r: int, c: int) -> int:
            return (r // 3) * 3 + (c // 3)

        # prepare sets and empty list
        row_sets = [set() for _ in range(N)]
        col_sets = [set() for _ in range(N)]
        box_sets = [set() for _ in range(N)]
        empties =  []

        for r in range(N):
            for c in range(N):
                ch = board[r][c]
                if ch == '.':
                    empties.append((r, c))
                else:
                    row_sets[r].add(ch)
                    col_sets[c].add(ch)
                    box_sets[box_index(r, c)].add(ch)

        # return available candidates set for (r,c)
        def candidates(r: int, c: int):
            used = row_sets[r] | col_sets[c] | box_sets[box_index(r, c)]
            return digits - used

        # backtracking with MRV: choose empty with fewest candidates
        def dfs(k: int) -> bool:
            if k == len(empties):
                return True

            # find index of empty with fewest candidates among empties[k:]
            best_i = -1
            best_cands = None
            best_cnt = 10
            for i in range(k, len(empties)):
                r, c = empties[i]
                cand = candidates(r, c)
                cnt = len(cand)
                if cnt == 0:
                    return False            # dead end early
                if cnt < best_cnt:
                    best_cnt = cnt
                    best_i = i
                    best_cands = cand
                    if cnt == 1:           # perfect cell, stop searching
                        break

            # move chosen empty to position k
            empties[k], empties[best_i] = empties[best_i], empties[k]
            r, c = empties[k]
            b = box_index(r, c)

            # iterate candidates (convert to list to avoid set mutation issues)
            for ch in list(best_cands):
                # place
                board[r][c] = ch
                row_sets[r].add(ch)
                col_sets[c].add(ch)
                box_sets[b].add(ch)

                if dfs(k + 1):
                    return True

                # undo
                board[r][c] = '.'
                row_sets[r].remove(ch)
                col_sets[c].remove(ch)
                box_sets[b].remove(ch)

            # swap back to restore order (not strictly required, but keeps state consistent)
            empties[k], empties[best_i] = empties[best_i], empties[k]
            return False

        dfs(0)



# --- Test Cases for your solveSudoku(board) implementation ---

def print_board(board):
    for r in board:
        print(' '.join(r))
    print()

def boards_equal(a, b):
    return all(a[r][c] == b[r][c] for r in range(9) for c in range(9))

def is_complete(board):
    return all(board[r][c] != '.' for r in range(9) for c in range(9))

def is_valid_completed_board(board):
    digits = set(str(i) for i in range(1,10))
    # rows
    for r in range(9):
        if set(board[r]) != digits:
            return False
    # cols
    for c in range(9):
        if set(board[r][c] for r in range(9)) != digits:
            return False
    # boxes
    for br in range(3):
        for bc in range(3):
            vals = []
            for r in range(br*3, br*3+3):
                for c in range(bc*3, bc*3+3):
                    vals.append(board[r][c])
            if set(vals) != digits:
                return False
    return True

# ---------------- Test cases ----------------

# 1) Standard LeetCode example (unique solution known)
board_1 = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
expected_1 = [
    ["5","3","4","6","7","8","9","1","2"],
    ["6","7","2","1","9","5","3","4","8"],
    ["1","9","8","3","4","2","5","6","7"],
    ["8","5","9","7","6","1","4","2","3"],
    ["4","2","6","8","5","3","7","9","1"],
    ["7","1","3","9","2","4","8","5","6"],
    ["9","6","1","5","3","7","2","8","4"],
    ["2","8","7","4","1","9","6","3","5"],
    ["3","4","5","2","8","6","1","7","9"]
]

# 2) Single-empty cell (trivial)
board_2 = [
    ["1","2","3","4","5","6","7","8","9"],
    ["4","5","6","7","8","9","1","2","3"],
    ["7","8","9","1","2","3","4","5","6"],
    ["2","3","4","5","6","7","8","9","1"],
    ["5","6","7","8","9","1","2","3","4"],
    ["8","9","1","2","3","4","5","6","7"],
    ["3","4","5","6","7","8","9","1","2"],
    ["6","7","8","9","1","2","3","4","5"],
    ["9","1","2","3","4","5","6","7","."]  # only this cell is empty
]
expected_2 = [
    ["1","2","3","4","5","6","7","8","9"],
    ["4","5","6","7","8","9","1","2","3"],
    ["7","8","9","1","2","3","4","5","6"],
    ["2","3","4","5","6","7","8","9","1"],
    ["5","6","7","8","9","1","2","3","4"],
    ["8","9","1","2","3","4","5","6","7"],
    ["3","4","5","6","7","8","9","1","2"],
    ["6","7","8","9","1","2","3","4","5"],
    ["9","1","2","3","4","5","6","7","8"]
]

# 3) Already solved (should remain unchanged)
board_3 = [row[:] for row in expected_1]

# 4) Invalid board (contradiction / unsolvable) — duplicate '5' in first row
board_4 = [
    ["5","5",".",".","7",".",".",".","."],  # invalid: two 5s in row 0
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

# 5) Medium-difficulty puzzle (checks general validity/completeness, solution not hard-coded)
board_5 = [
    [".",".","9","7","4","8",".",".","."],
    ["7",".",".",".",".",".",".",".","."],
    [".","2",".","1",".","9",".",".","."],
    [".",".","7",".",".",".","2","4","."],
    [".","6","4",".","1",".","5","9","."],
    [".","9","8",".",".",".","3",".","."],
    [".",".",".","8",".","3",".","2","."],
    [".",".",".",".",".",".",".",".","6"],
    [".",".",".","2","7","5","9",".","."]
]

# 6) Another valid puzzle with multiple clues (useful for performance)
board_6 = [
    [".",".","6","3",".",".",".",".","."],
    [".",".",".",".",".",".",".","1","."],
    [".",".","9",".",".",".","4",".","."],
    [".",".",".",".",".",".",".",".","7"],
    [".",".",".",".","8",".",".",".","."],
    [".",".",".",".",".","1",".",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".","1",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."]
]

tests = [
    ("LeetCode example", board_1, expected_1),
    ("Single empty", board_2, expected_2),
    ("Already solved", board_3, expected_1),
    ("Invalid input (contradiction)", board_4, None),
    ("Medium puzzle (validity check)", board_5, None),
    ("Loose clues (completeness check)", board_6, None),
]

# ---------- runner ----------
for name, board, expected in tests:
    b = [row[:] for row in board]  # copy so original stays intact
    print("Running:", name)
    print("Before:")
    print_board(b)
    solveSudoku(b)
    print("After:")
    print_board(b)

    if expected is not None:
        assert boards_equal(b, expected), f"{name} failed: result != expected"
        print(name, "passed (matches expected).\n")
    else:
        # For tests where we didn't hardcode the solution, check completeness & validity
        if is_complete(b) and is_valid_completed_board(b):
            print(name, "passed (completed and valid).\n")
        else:
            print(name, "NOT solved to a valid completed board (this may be expected for invalid inputs).\n")

print("All tests finished.")
