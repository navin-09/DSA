from sieve_spf import sieve_spf

def factorize(x, spf):
    factors = []
    while x != 1:
        factors.append(spf[x])
        x //= spf[x]
    return factors

spf = sieve_spf(100)
print(factorize(84, spf))  # [2, 2, 3, 7]
