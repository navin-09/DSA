def swap(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b

x, y = swap(5, 9)
print(x, y)  # 9 5
