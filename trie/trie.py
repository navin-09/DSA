class TrieNode:
    def __init__(self):
        self.children = {}     # map from char → TrieNode
        self.is_end = False    # marks end of a word


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True

    def delete(self, word: str) -> None:
        def helper(node, word, depth):
            if not node:
                return False
            if depth == len(word):
                if not node.is_end:
                    return False
                node.is_end = False
                return len(node.children) == 0
            ch = word[depth]
            if ch in node.children and helper(node.children[ch], word, depth + 1):
                del node.children[ch]
                return not node.is_end and len(node.children) == 0
            return False
        helper(self.root, word, 0)

# Create a Trie
trie = Trie()

# Insert words
trie.insert("cat")
trie.insert("car")
trie.insert("dog")

# Search exact words
print(trie.search("car"))   # ✅ True
print(trie.search("cap"))   # ❌ False

# Prefix check
print(trie.startsWith("ca"))  # ✅ True

# Delete a word
trie.delete("car")
print(trie.search("car"))   # ❌ False
print(trie.search("cat"))   # ✅ True (still there)
