# Count almost equal pairs i

[Problem link](https://leetcode.com/problems/count-almost-equal-pairs-i/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/count-almost-equal-pairs-i/

class Solution:
    def countPairs(self, nums: List[int]) -> int:
        def swaps(n, ret):
            s = str(n)
            l = len(s)
            for i in range(l):
                for j in range(i):
                    if s[i] == s[j]:
                        continue
                    ret.add(int(s[:j] + s[i] + s[j+1:i] + s[j] + s[i+1:]))
            return ret

        options = [swaps(x, set([x])) for x in nums]
        n = len(nums)
        ret = 0
        for i in range(n):
            for j in range(i):
                if nums[i] in options[j] or nums[j] in options[i]:
                    ret += 1
        return ret
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap)
