def build_pascals_triangle(n):
    C = [[0]*(n+1) for _ in range(n+1)]
    for i in range(n+1):
        for j in range(i+1):
            if j == 0 or j == i:
                C[i][j] = 1
            else:
                C[i][j] = C[i-1][j-1] + C[i-1][j]
    return C

def print_pascals_pattern(n):
    triangle = build_pascals_triangle(n)
    width = n * 4  # spacing for centering
    for i in range(n+1):
        row = [str(x) for x in triangle[i][:i+1]]
        print(' '.join(row).center(width))

print_pascals_pattern(5)
print(build_pascals_triangle(5))
