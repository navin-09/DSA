def sieve_prime(num):
    primes = [True]*(num+1)
    primes[0] = primes[1] = False
    for i in range(2, int(num**0.5)+1):
        if (primes[i]):
            for j in range(i*i,num+1, i):
                primes[j] = False
    return primes

print(sum(sieve_prime(100)))
