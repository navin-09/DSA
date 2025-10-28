def number_to_column_title(n):
    result = []
    while n > 0:
        n -= 1                      # adjust for 1-indexed system
        result.append(chr(n % 26 + ord('A')))  # get corresponding letter
        n //= 26
    return ''.join(reversed(result))


print(number_to_column_title(1))    # A
print(number_to_column_title(28))   # AB
print(number_to_column_title(701))  # ZY
print(number_to_column_title(703))  # AAA