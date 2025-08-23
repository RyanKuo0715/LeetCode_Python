# LeetCode Problem 208: Implement Trie (Prefix Tree)
# https://leetcode.com/problems/implement-trie-prefix-tree/description/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.ds = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.ds
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        cur.end = True

    def search(self, word: str) -> bool:
        cur = self.ds
        for ch in word:
            if ch not in cur.children:
                return False
            else:
                cur = cur.children[ch]
        return cur.end

    def startsWith(self, prefix: str) -> bool:
        cur = self.ds
        for ch in prefix:
            if ch not in cur.children:
                return False
            else:
                cur = cur.children[ch]
        return True

# class Trie:
#     def __init__(self):
#         self.ds = []

#     def insert(self, word: str) -> None:
#         self.ds.append(word)

#     def search(self, word: str) -> bool:
#         return word in self.ds

#     def startsWith(self, prefix: str) -> bool:
#         for word in self.ds:
#             if word.startswith(prefix):
#                 return True
#         return False

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
