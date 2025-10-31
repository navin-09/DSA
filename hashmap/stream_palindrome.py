def stream_palindrome(stream: str):
    """
    For each incoming character, determine if the current prefix
    (stream so far) forms a palindrome using forward and reverse hashes.
    """

    base = 256
    mod = 10**9 + 7

    f_hash = 0  # forward hash
    r_hash = 0  # reverse hash
    power = 1   # base^(len-1) used to align reverse hash
    res = []

    for ch in stream:
        val = ord(ch)

        # Update forward hash: append character to the right
        f_hash = (f_hash * base + val) % mod

        # Update reverse hash: append character to the left
        # equivalent to val * base^(current_length) + previous_reverse
        r_hash = (r_hash + val * power) % mod

        # Compare hashes — if equal, likely palindrome
        res.append(f_hash == r_hash)

        # Increase power for next position
        power = (power * base) % mod

    return res


# Example
stream = "abbae"
print(stream_palindrome(stream))
# Output: [True, False, False, True, False]
