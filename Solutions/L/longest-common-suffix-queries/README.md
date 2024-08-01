# Longest common suffix queries

[Problem link](https://leetcode.com/problems/longest-common-suffix-queries/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/longest-common-suffix-queries/

class Node:
    def __init__(self):
        self.children = {}
        self.best = (inf, inf)

    def insert(self, s, l, idx, pos):
        self. best = min(self. best, (l, idx))
        if pos == -1:
            return
        if s[pos] not in self.children:
            self.children[s[pos]] = Node()
        self.children[s[pos]]. insert(s, l, idx, pos-1)

    def query(self, s, pos):
        if pos == -1 or s[pos] not in self. children:
            return self. best[1]
        return self. children[s[pos]]. query(s, pos - 1)


class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        trie = Node()
        for i, x in enumerate(wordsContainer):
            trie . insert(x, len(x), i, len(x) - 1)
        return [trie.query(x, len(x) - 1) for x in wordsQuery]
```
## Tags

* [Trie](/Collections/trie.md#trie)
* [String](/Collections/string.md#string) > [Search](/Collections/string.md#search) > [Trie](/Collections/string.md#trie)
