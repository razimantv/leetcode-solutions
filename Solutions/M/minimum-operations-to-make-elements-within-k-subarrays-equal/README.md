# Minimum operations to make elements within k subarrays equal

[Problem link](https://leetcode.com/problems/minimum-operations-to-make-elements-within-k-subarrays-equal/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/minimum-operations-to-make-elements-within-k-subarrays-equal/


class Solution:
    def minOperations(self, nums: list[int], p: int, k: int) -> int:
        l, r, balance = SortedList(), SortedList(), [inf] * (n := len(nums))
        lsum, rsum = 0, 0

        def equalise():
            nonlocal lsum, rsum
            while len(r) - len(l) > 1:
                y = r.pop(0)
                rsum -= y
                l.add(y)
                lsum += y
            while len(l) > len(r):
                y = l.pop(-1)
                lsum -= y
                r.add(y)
                rsum += y

        for i, x in enumerate(nums):
            if len(r) and x >= r[0]:
                r.add(x)
                rsum += x
            else:
                l.add(x)
                lsum += x
            equalise()
            if i >= p - 1:
                m = r[0]
                balance[i] = (m * len(l) - lsum) + (rsum - len(r) * m)
                y = nums[i - p + 1]

                if y >= m:
                    r.remove(y)
                    rsum -= y
                else:
                    l.remove(y)
                    lsum -= y
                equalise()
        dp = [0] * (n + 1)
        for i in range(k):
            newdp = [inf] * p
            for j in range(p - 1, n):
                newdp.append(min(newdp[-1], dp[j - p + 1] + balance[j]))
            dp = newdp
        return dp[-1]
```
## Tags

* [Mathematics](/Collections/mathematics.md#mathematics) > [Median](/Collections/mathematics.md#median)
* [Priority queue](/Collections/priority-queue.md#priority-queue) > [K smallest/largest elements](/Collections/priority-queue.md#k-smallest-largest-elements) > [Transfer between the two](/Collections/priority-queue.md#transfer-between-the-two)
* [Priority queue](/Collections/priority-queue.md#priority-queue) > [Python SortedList](/Collections/priority-queue.md#python-sortedlist)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Array reuse](/Collections/dynamic-programming.md#array-reuse)
