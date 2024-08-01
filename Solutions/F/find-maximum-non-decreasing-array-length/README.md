# Find maximum non decreasing array length

[Problem link](https://leetcode.com/problems/find-maximum-non-decreasing-array-length/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/find-maximum-non-decreasing-array-length/

class Solution:
    def findMaximumLength(self, nums: List[int]) -> int:
        # dp(i) = max number of valid subarrays of [0...i]
        # monotonic: dp(i) >= dp(i-1)
        # dp2(i) = minimum last subarray sum in valid split
        # dp(i) = 1 + dp(i') : sum(a(i'+1...i)) > dp2(i')
        # => psum(i) >= psum(i') + dp2(i')
        mono = [(0, 0, 0, 0)]  # dp, dp2, psum, cond
        ptr = 0
        for x in nums:
            psum = mono[-1][2] + x
            while ptr < len(mono) and psum >= mono[ptr][-1]:
                ptr += 1
            ptr -= 1
            dp, dp2, psum_, cond = mono[ptr]
            dp += 1
            dp2 = psum - psum_
            cond = psum + dp2
            while mono[-1][-1] >= cond:
                mono.pop()
            mono.append((dp, dp2, psum, cond))
        return mono[-1][0]
```
## Tags

* [Deque](/Collections/deque.md#deque) > [Monotonic deque](/Collections/deque.md#monotonic-deque)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Monotonic stack/deque](/Collections/dynamic-programming.md#monotonic-stack-deque)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Expression rearrangement](/Collections/mathematics.md#expression-rearrangement)
* [Prefix](/Collections/prefix.md#prefix) > [Sum](/Collections/prefix.md#sum)
