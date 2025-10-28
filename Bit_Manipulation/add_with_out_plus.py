MASK = 0xFFFFFFFF
MAX_INT = 0x7FFFFFFF

def add(a, b):
    while b != 0:
        a, b = (a ^ b) & MASK, ((a & b) << 1) & MASK

    # if a is negative in 32-bit form
    return a if a <= MAX_INT else ~(a ^ MASK)

def subtract(a, b):
    return add(a, add(~b, 1))

print(add(5, 7))        # 12
print(subtract(10, 4))  # 6
print(subtract(4, 10))  # -6

# twos complement of 'a is ~a + 1'
# -a  => ~a + 1
