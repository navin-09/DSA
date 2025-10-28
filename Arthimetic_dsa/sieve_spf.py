def sieve_spf(n):
    spf = [0] * (n + 1)       # spf[i] = smallest prime factor of i
    for i in range(2, n + 1):
        spf[i] = i            # initially assume each number is its own factor

    for i in range(2, int(n**0.5) + 1):
        if spf[i] == i:       # i is prime
            for j in range(i * i, n + 1, i):
                if spf[j] == j:  # not yet marked
                    spf[j] = i   # mark i as smallest factor
    return spf

spf = sieve_spf(30)
print(spf[2:])
# Output: [2, 3, 2, 5, 2, 7, 2, 3, 2, 11, 2, 13, 2, 3, 2, 17, 2, 19, 2, 3, 2, 23, 2, 5, 2, 3, 2, 29, 2]
