def nfibno(n):
    if n == 0:return 0
    if n == 1:return 1
    return nfibno(n-2)+nfibno(n-1)

print(nfibno(7)) # 0 1 1 2 3 5 8 13