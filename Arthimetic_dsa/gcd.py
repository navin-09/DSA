def gcd_i(a, b):
    while b:
        a, b = b, a % b
    return a

def gcd_r(a,b):
    if b == 0:
        return a
    return gcd_r(b,a%b)


print(gcd_r(12,34))

# gcd(a,b) = gcd(b,a%b)