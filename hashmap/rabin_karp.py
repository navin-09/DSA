def rabin_karp_all(text: str, pattern: str):
    """
    Rabin-Karp string matching algorithm.
    Finds all starting indices where 'pattern' occurs in 'text'.

    The idea:
    Treat each substring (window) as a number in base 'base' system.
    Example: 'abc' → a*base^2 + b*base^1 + c*base^0
    As we slide one position right, we update the hash efficiently
    using the precomputed highest power (base^(m-1)).
    """

    # Edge case handling
    if pattern == "":
        return list(range(len(text) + 1))
    
    n, m = len(text), len(pattern)
    if m > n:
        return []

    base = 256             # "place value" base (like 10 in decimal)
    mod = 10**9 + 7        # large prime to avoid overflow
    res = []

    # Precompute base^(m-1) % mod
    # This represents the "weight" of the leftmost character in the window.
    high_pow = pow(base, m - 1, mod)

    # Compute hash for pattern and the first window of text
    pattern_hash = 0
    window_hash = 0
    for i in range(m):
        pattern_hash = (pattern_hash * base + ord(pattern[i])) % mod
        window_hash = (window_hash * base + ord(text[i])) % mod

    # Slide the window across the text
    for j in range(n - m + 1):
        # If hashes match, double-check the actual substring
        if pattern_hash == window_hash and text[j:j + m] == pattern:
            res.append(j)

        if j < n - m:
            # 🔹 Step 1: Remove contribution of leftmost char
            #    text[j] was multiplied by base^(m-1), so subtract that part.
            window_hash = (window_hash - ord(text[j]) * high_pow) % mod

            # 🔹 Step 2: Shift all remaining characters left by multiplying by base
            #    This increases each power by 1 (like moving digits left).
            window_hash = (window_hash * base) % mod

            # 🔹 Step 3: Add the new character at the right (lowest power, base^0)
            window_hash = (window_hash + ord(text[j + m])) % mod

    return res


# Example
print(rabin_karp_all("banana", "ana"))  # -> [1, 3]
