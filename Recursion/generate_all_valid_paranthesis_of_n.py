from typing import List

def generate_parentheses(n: int) -> List[str]:
    result = []

    def backtrack(s: str, open_left: int, close_left: int):
        # ✅ Base case: when no brackets left to add
        if open_left == 0 and close_left == 0:
            result.append(s)
            return

        # 🟢 Add '(' if we still can
        if open_left > 0:
            backtrack(s + '(', open_left - 1, close_left)

        # 🔵 Add ')' only if there are more closes left than opens
        if close_left > open_left:
            backtrack(s + ')', open_left, close_left - 1)

    # Start with n opens and n closes
    backtrack('', n, n)
    return result


# Example
print(f"n=3: {generate_parentheses(3)}")
