from functools import cache
from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def buildTrie(root, word):
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.is_end = True

        root = TrieNode()
        for word in wordDict:
            buildTrie(root, word)

        @cache
        def dfs(i):
            if i == len(s):
                return True
            node = root
            for j in range(i, len(s)):
                ch = s[j]
                if ch not in node.children:
                    break
                node = node.children[ch]
                if node.is_end and dfs(j + 1):
                    return True
            return False

        return dfs(0)


# ✅ Test cases
if __name__ == "__main__":
    sol = Solution()

    print(sol.wordBreak("leetcode", ["leet", "code"]))        # True
    print(sol.wordBreak("applepenapple", ["apple", "pen"]))   # True
    print(sol.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))  # False
    print(sol.wordBreak("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]))  # True
    print(sol.wordBreak("cars", ["car", "ca", "rs"]))         # True
