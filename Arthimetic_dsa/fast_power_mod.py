def fast_power_mod(a, b, mod):
    result = 1
    a %= mod  # reduce base once at start
    while b > 0:
        if b & 1:
            result = (result * a) % mod
        a = (a * a) % mod
        b = b >> 1
    return result

def fast_power_mod_rec(base, exp, mod):
    if exp == 0:
        return 1
    half = fast_power_mod_rec(base, exp // 2, mod)
    
    if exp % 2 == 0:
        return (half * half) % mod
    else:
        return (half * half * base) % mod

print(fast_power_mod(3, 13, 7))    # (3^13) % 7 = 5
print(fast_power_mod(2, 100, 13))  # (2^100) % 13 = 9
