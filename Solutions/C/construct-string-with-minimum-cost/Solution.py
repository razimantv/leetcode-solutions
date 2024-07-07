# https://leetcode.com/problems/construct-string-with-minimum-cost/

class Node:
    def __init__(self):
        self.children = {}
        self.cost = math.inf

    def insert(self, s, pos, cost):
        if pos == len(s):
            self.cost = min(self.cost, cost)
            return
        if s[pos] not in self.children:
            self.children[s[pos]] = Node()
        self.children[s[pos]].insert(s, pos + 1, cost)


class Solution:
    def minimumCost(
        self, target: str, words: List[str], costs: List[int]
    ) -> int:
        trie = Node()
        for word, cost in zip(words, costs):
            trie.insert(word, 0, cost)

        n = len(target)
        dp = [math.inf] * n + [0]
        for i in range(n - 1, -1, -1):
            cur = trie
            for j in range(i, n):
                if target[j] not in cur.children:
                    break
                cur = cur.children[target[j]]
                dp[i] = min(dp[i], cur.cost + dp[j + 1])
        return -1 if dp[0] > 10 ** 10 else dp[0]
