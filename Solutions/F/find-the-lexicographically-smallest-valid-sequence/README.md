# Find the lexicographically smallest valid sequence

[Problem link](https://leetcode.com/problems/find-the-lexicographically-smallest-valid-sequence/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/find-the-lexicographically-smallest-valid-sequence/

class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        m, n = len(word1), len(word2)
        suf = [n] * (m + 1)
        next = n - 1
        for i in range(m - 1, -1, -1):
            if next != -1 and word1[i] == word2[next]:
                next -= 1
            suf[i] = next + 1

        ret, flag, next = [], True, 0
        for i, c in enumerate(word1):
            if c == word2[next]:
                ret.append(i)
                next += 1
            elif flag and suf[i + 1] <= next + 1:
                flag = False
                ret.append(i)
                next += 1
            if next == n:
                return ret
        return []
```
## Tags

* [Array scanning](/Collections/array-scanning.md#array-scanning) > [From both ends of array](/Collections/array-scanning.md#from-both-ends-of-array)
* [Greedy](/Collections/greedy.md#greedy)
* [String](/Collections/string.md#string) > [Subsequence](/Collections/string.md#subsequence)
