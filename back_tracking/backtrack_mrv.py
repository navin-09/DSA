def backtrack_mrv(board):
    empties = collect_empty_cells(board)
    # helper to compute candidates for a cell
    def candidates(cell):
        # return set/list of valid candidates quickly
        pass

    def dfs(k):
        if k == len(empties):
            return True
        # pick best empty among empties[k:]
        best_idx, best_cands = None, None
        best_cnt = 10
        for i in range(k, len(empties)):
            cands = candidates(empties[i])
            if not cands:
                return False
            if len(cands) < best_cnt:
                best_cnt = len(cands)
                best_idx = i
                best_cands = cands
                if best_cnt == 1:
                    break
        empties[k], empties[best_idx] = empties[best_idx], empties[k]
        r, c = empties[k]

        for val in list(best_cands):
            place(r, c, val)
            if dfs(k+1):
                return True
            undo(r, c, val)
        empties[k], empties[best_idx] = empties[best_idx], empties[k]
        return False

    dfs(0)
