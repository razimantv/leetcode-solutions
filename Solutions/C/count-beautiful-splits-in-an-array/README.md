# Count beautiful splits in an array

[Problem link](https://leetcode.com/problems/count-beautiful-splits-in-an-array)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/count-beautiful-splits-in-an-array

class Solution:
    def beautifulSplits(self, nums: List[int]) -> int:
        n = len(nums)
        groups, blocked = [set(range(-1, n - 1))], set()

        def process(groups, L):
            ret = 0
            for group in groups:
                for x in sorted(group):
                    if x - L in group:
                        if x == 2 * L - 1:
                            blocked.add(L)
                            ret += n - 1 - x
                        elif x - 2 * L + 1 not in blocked:
                            ret += 1
            return ret

        def extend(groups, n):
            ret = defaultdict(set)
            for g, group in enumerate(groups):
                for i in group:
                    if i < n - 1:
                        ret[(g, nums[i + 1])].add(i + 1)
            return [group for group in ret.values() if len(group) > 1]

        ret, L = 0, 1
        while groups:
            groups = extend(groups, n)
            ret += process(groups, L)
            L += 1
        return ret
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Length-wise processing](/Collections/dynamic-programming.md#length-wise-processing)
* [Hashmap](/Collections/hashmap.md#hashmap) > [Group items](/Collections/hashmap.md#group-items)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Array reuse](/Collections/dynamic-programming.md#array-reuse)
