from Arthimetic_dsa import factorial

def nPr(n, r):
    return factorial(n) // factorial(n - r)

def nCr(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

print(nPr(5, 2))  # 20
print(nCr(5, 2))  # 10
