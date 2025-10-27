def is_even(num):
    return (num & 1) == 0


def is_odd(num):
    return (num & 1) == 1

print('is_even',is_even(2))
print('is_even',is_even(3))

print('is_odd',is_odd(2))
print('is_odd',is_odd(3))
