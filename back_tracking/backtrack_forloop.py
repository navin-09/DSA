def backtrack_forloop(arr, k):
    res = []
    n = len(arr)

    def dfs(start, path):
        res.append(path[:])     # could record at every node
        for i in range(start, n):
            path.append(arr[i])
            dfs(i + 1, path)   # next choose after i
            path.pop()

    dfs(0, [])
    return res
