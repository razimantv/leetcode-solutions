# Combination sum ii

[Problem link](https://leetcode.com/problems/combination-sum-ii/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/combination-sum-ii/

class Solution:
    def combinationSum2(
        self, candidates: List[int], target: int
    ) -> List[List[int]]:
        candidates = sorted(list(Counter(candidates).items()))
        n, ret = len(candidates), []

        def backtrack(target, i, cur):
            if not target:
                ret.append(cur.copy())
                return
            elif i == n:
                return

            x, cnt = candidates[i]
            cnt = min(cnt, target // x)
            if not cnt:
                return
            for c in range(cnt + 1):
                backtrack(target, i + 1, cur)
                cur.append(x)
                target -= x
            while cur and cur[-1] == x:
                cur.pop()
        backtrack(target, 0, [])
        return ret
```
## Tags

* [Backtracking](/Collections/backtracking.md#backtracking) > [Push and pop for efficient state update](/Collections/backtracking.md#push-and-pop-for-efficient-state-update)
* [Hashmap](/Collections/hashmap.md#hashmap) > [Counter](/Collections/hashmap.md#counter)
