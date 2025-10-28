# DSA
(a+b) % m ==> (a%m + b%m) % m
(a-b) % m ==> (a%m - b%m) % m
(a*b) % m ==> (a%m * b%m) % m

| Problem Type               | Formula               | Notes                   |
| -------------------------- | --------------------- | ----------------------- |
| Arrange r from n           | nPr = n! / (n-r)!     | Order matters           |
| Choose r from n            | nCr = n! / (r!(n-r)!) | Order doesn’t           |
| With repetition            | n^r                   | Each choice independent |
| Circular                   | (n-1)!                | Rotation same           |
| Identical objects          | n! / (p!q!r!...)      | Divide by repeats       |
| Distribute identical items | C(r+n-1, n-1)         | Stars and bars          |


# recursion
def function(parameter):
    if base_condition:          # 🛑 stopping condition
        return result
    smaller_result = function(smaller_parameter)  # 🔁 recursive call solve subproblem
    return combine(smaller_result)
