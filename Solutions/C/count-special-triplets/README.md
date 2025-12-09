# Count special triplets

[Problem link](https://leetcode.com/problems/count-special-triplets/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/count-special-triplets/

class Solution:
    def specialTriplets(self, nums: list[int]) -> int:
        cnt = [Counter() for _ in range(3)]
        for x in nums[::-1]:
            if x % 2 == 0:
                cnt[2][x] += cnt[1][x // 2]
            cnt[1][x] += cnt[0][2 * x]
            cnt[0][x] += 1
        return sum(cnt[2]. values()) % (10 ** 9 + 7)
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap) > [Counter](/Collections/hashmap.md#counter)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Array reuse](/Collections/dynamic-programming.md#array-reuse)
