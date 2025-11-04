def backtrack_binary(arr):
    res = []
    n = len(arr)

    def dfs(i, path):
        if i == n:
            res.append(path[:])   # record one solution
            return
        # choose arr[i]
        path.append(arr[i])
        dfs(i + 1, path)
        path.pop()
        # skip arr[i]
        dfs(i + 1, path)

    dfs(0, [])
    return res
