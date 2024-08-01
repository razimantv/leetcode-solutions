# Find beautiful indices in the given array i

[Problem link](https://leetcode.com/problems/find-beautiful-indices-in-the-given-array-i/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/find-beautiful-indices-in-the-given-array-i/

class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        def matches(haystack, needle):
            p1, p2 = 43, 10 ** 9 + 7
            ln, lh = len(needle), len(haystack)
            nhash, p1pow = 0, 1
            for c in needle:
                nhash = (nhash * p1 + ord(c) - ord('a')) % p2
                p1pow = (p1pow * p1) % p2

            l, hhash, ret = 0, 0, []
            for r, c in enumerate(haystack):
                hhash = (hhash * p1 + ord(c) - ord('a')) % p2
                if r - l == ln:
                    hhash = (
                        hhash + p2 -
                        (p1pow * (ord(haystack[l]) - ord('a'))) % p2
                    ) % p2
                    l += 1
                if r >= ln - 1 and hhash == nhash:
                    ret.append(r - ln + 1)
            return ret

        ma, mb = matches(s, a), matches(s, b)
        lb, ib, ret = len(mb), 0, []
        for x in ma:
            while ib < lb and mb[ib] < x - k:
                ib += 1
            if ib >= lb:
                break
            if mb[ib] <= x + k:
                ret.append(x)
        return ret
```
## Tags

* [String](/Collections/string.md#string) > [Search](/Collections/string.md#search) > [Hashing](/Collections/string.md#hashing)
* [Sliding window](/Collections/sliding-window.md#sliding-window) > [String hashing](/Collections/sliding-window.md#string-hashing)
