def backtrack_grid(board, start_r, start_c, target):
    m, n = len(board), len(board[0])
    visited = [[False]*n for _ in range(m)]

    def dfs(r, c, state):
        if goal(state):
            return True
        for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
            nr, nc = r+dr, c+dc
            if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc] and valid(board[nr][nc], state):
                visited[nr][nc] = True
                if dfs(nr, nc, update(state, board[nr][nc])):
                    return True
                visited[nr][nc] = False
        return False

    visited[start_r][start_c] = True
    return dfs(start_r, start_c, initial_state)
