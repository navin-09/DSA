def fast_power(a, b):
    result = 1
    while b > 0:
        if b & 1:         # if the current bit is 1
            result = result * a
        a = a * a             # square the base
        b = b >> 1            # move to next bit
    return result

def fast_power_rec(base, exp):
    if exp == 0:
        return 1
    half = fast_power_rec(base, exp // 2)
    
    if exp % 2 == 0:
        return half * half
    else:
        return base * half * half

print(fast_power_rec(3,100))