# https://leetcode.com/problems/minimum-number-of-valid-strings-to-form-target-i/

class Node:
    def __init__(self):
        self.children = {}

    def insert(self, word, i, n):
        if i == n:
            return

        c = word[i]
        if c not in self.children:
            self.children[c] = Node()
        self.children[c].insert(word, i + 1, n)


class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        trie = Node()
        for word in words:
            trie.insert(word, 0, len(word))

        n = len(target)
        dp = [n + 1] * n + [0]
        for i in range(n - 1, -1, -1):
            cur = trie
            for j in range(i, n):
                if target[j] in cur.children:
                    cur = cur.children[target[j]]
                    dp[i] = min(dp[i], dp[j + 1] + 1)
                else:
                    break
        return dp[0] if dp[0] <= n else -1
