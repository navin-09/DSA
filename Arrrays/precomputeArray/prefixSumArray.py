class PrefixSum:
    def calculate_prefix(self, arr: list[int]) -> list[int]:
        """
        Calculate the prefix sum of a given list of integers.
        Example: [-4, -3, -2] -> [-4, -7, -9]
        """
        n = len(arr)
        if n == 0:
            return []

        prefix_sum = [arr[0]]
        for i in range(1, n):
            prefix_sum.append(prefix_sum[-1] + arr[i])

        return prefix_sum


# Example usage
prefix = PrefixSum()
result = prefix.calculate_prefix([-4, -3, -2, -1, 0, 1, 2, 3, 4])
print(result)
