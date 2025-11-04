def backtrack_permute(arr):
    n = len(arr)
    res = []
    used = [False] * n

    def dfs(path):
        if len(path) == n:
            res.append(path[:])
            return
        for i in range(n):
            if used[i]:
                continue
            used[i] = True
            path.append(arr[i])
            dfs(path)
            path.pop()
            used[i] = False

    dfs([])
    return res
