# Count elements with maximum frequency

[Problem link](https://leetcode.com/problems/count-elements-with-maximum-frequency/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/count-elements-with-maximum-frequency/

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        ctr = Counter(nums)
        mx = max(ctr.values())
        return sum(x for x in ctr.values() if x == mx)
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap) > [Counter](/Collections/hashmap.md#counter)
