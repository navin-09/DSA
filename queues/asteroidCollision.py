from typing import List

def asteroidCollision(asteroids: List[int]) -> List[int]:
    stack: List[int] = []

    for a in asteroids:
        destroyed = False
        # Only possible collision: stack top > 0 (moving right) and a < 0 (moving left)
        while stack and stack[-1] > 0 and a < 0:
            top = stack[-1]
            if abs(top) < abs(a):
                # top explodes; pop and continue checking
                stack.pop()
                continue
            elif abs(top) == abs(a):
                # both explode
                stack.pop()
                destroyed = True
                break
            else:
                # current asteroid explodes
                destroyed = True
                break

        if not destroyed:
            stack.append(a)

    return stack


print(asteroidCollision([5, 10, -5]))     # [5, 10]        (10 destroys -5)
print(asteroidCollision([8, -8]))         # []             (equal sizes destroy)
print(asteroidCollision([10, 2, -5]))     # [10]           (2 destroyed by -5; -5 destroyed by 10? actually 10 and -5 don't meet)
print(asteroidCollision([-2, -1, 1, 2]))  # [-2, -1, 1, 2] (no head-on collisions)
print(asteroidCollision([1, -2, -2, -2])) # [-2, -2, -2]   (1 destroyed by first -2)
