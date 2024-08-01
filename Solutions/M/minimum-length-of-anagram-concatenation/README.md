# Minimum length of anagram concatenation

[Problem link](https://leetcode.com/problems/minimum-length-of-anagram-concatenation/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/minimum-length-of-anagram-concatenation/

class Solution:
    def minAnagramLength(self, s: str) -> int:
        n = len(s)
        s = [ord(c) - ord('a') for c in s]

        def work(k):
            first = [0] * 26
            for c in s[:k]:
                first[c] += 1

            for start in range(k, n, k):
                cur = [0] * 26
                for c in s[start: start+k]:
                    cur[c] += 1
                    if cur[c] > first[c]:
                        return False
            return True

        bigfac, f = [], 1
        while f * f <= n:
            if n % f == 0:
                if 1 < f * f < n:
                    bigfac.append(n // f)
                if work(f):
                    return f
            f += 1
        for f in bigfac[::-1]:
            if work(f):
                return f
        return n
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap) > [Counter](/Collections/hashmap.md#counter)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Number theory](/Collections/mathematics.md#number-theory) > [Factor listing in sqrt(N)](/Collections/mathematics.md#factor-listing-in-sqrt-n-)
