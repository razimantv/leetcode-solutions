# Subarrays with k different integers

[Problem link](https://leetcode.com/problems/subarrays-with-k-different-integers/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/subarrays-with-k-different-integers/

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        n = len(nums)

        def first(k):
            ret, left = [], -1
            cnt = defaultdict(int)
            for x in nums:
                cnt[x] += 1
                while len(cnt) > k:
                    left += 1
                    cnt[nums[left]] -= 1
                    if cnt[nums[left]] == 0:
                        cnt.pop(nums[left])
                ret. append(left)
            return ret

        return sum(y-x for x, y in zip(first(k), first(k-1)))
```
## Tags

* [Sliding window](/Collections/sliding-window.md#sliding-window)
* [Hashmap](/Collections/hashmap.md#hashmap) > [Counter](/Collections/hashmap.md#counter)
