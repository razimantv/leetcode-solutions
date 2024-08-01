# Find the length of the longest common prefix

[Problem link](https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        seen = defaultdict(int)
        for x in arr1:
            l = len(str(x))
            while x:
                seen[x] = l
                l -= 1
                x //= 10

        ret = 0
        for x in arr2:
            while x:
                ret = max(ret, seen[x])
                x //= 10

        return ret
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap)
