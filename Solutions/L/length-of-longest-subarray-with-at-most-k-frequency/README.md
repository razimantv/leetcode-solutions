# Length of longest subarray with at most k frequency

[Problem link](https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n, l, best = len(nums), 0, 0
        cnt = defaultdict(int)
        for r in range(n):
            cnt[nums[r]] += 1
            while cnt[nums[r]] > k:
                cnt[nums[l]] -= 1
                l += 1
            best = max(best, r - l + 1)
        return best
```
## Tags

* [Sliding window](/Collections/sliding-window.md#sliding-window)
* [Hashmap](/Collections/hashmap.md#hashmap)
