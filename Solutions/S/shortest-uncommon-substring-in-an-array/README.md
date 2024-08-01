# Shortest uncommon substring in an array

[Problem link](https://leetcode.com/problems/shortest-uncommon-substring-in-an-array/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/shortest-uncommon-substring-in-an-array/

class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        seen = {}
        for w, word in enumerate(arr):
            l = len(word)
            for i in range(l):
                for j in range(i + 1):
                    cur = word[j:i+1]
                    if cur not in seen:
                        seen[cur] = w
                    elif seen[cur] != w:
                        seen[cur] = -1

        ret = []
        for w, word in enumerate(arr):
            best, l = "", len(word)
            for i in range(1, l+1):
                for j in range(l - i + 1):
                    cur = word[j:j+i]
                    if seen[cur] == w and (not best or best > cur):
                        best = cur
                if best:
                    break
            ret.append(best)
        return ret
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap)
* [String](/Collections/string.md#string) > [Search](/Collections/string.md#search)
