# Maximum total subarray value ii

[Problem link](https://leetcode.com/problems/maximum-total-subarray-value-ii/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/maximum-total-subarray-value-ii/

class Solution:
    def maxTotalValue(self, nums: list[int], k: int) -> int:
        def work(diff):
            monoinc, monodec = [-1], [-1]
            incsum, decsum = [0], [0]
            last, p1, p2, cnt, tot = -1, 1, 1, 0, 0
            for i, x in enumerate(nums):
                while monoinc[-1] > -1 and x <= nums[monoinc[-1]]:
                    monoinc.pop()
                    incsum.pop()
                    p1 = min(p1, len(monoinc))
                while monodec[-1] > -1 and x >= nums[monodec[-1]]:
                    monodec.pop()
                    decsum.pop()
                    p2 = min(p2, len(monodec))
                incsum.append(incsum[-1] + (i - monoinc[-1]) * x)
                decsum.append(decsum[-1] + (i - monodec[-1]) * x)
                monoinc.append(i)
                monodec.append(i)

                while last + 1 <= i and nums[monodec[p2]] - nums[monoinc[p1]] >= diff:
                    last = min(monodec[p2], monoinc[p1])
                    if monoinc[p1] == last:
                        p1 += 1
                    if monodec[p2] == last:
                        p2 += 1
                cnt += last + 1
                tot += (decsum[-1] - incsum[-1]) if last == i else (
                    (decsum[p2] - (monodec[p2] - last) * nums[monodec[p2]]) - 
                    (incsum[p1] - (monoinc[p1] - last) * nums[monoinc[p1]])
                )
            return cnt, tot

        start, end = 0, max(nums) - min(nums) + 1
        while end - start > 1:
            mid = (start + end) // 2
            if work(mid)[0] >= k:
                start = mid
            else:
                end = mid
        
        cnt, tot = work(start)
        return tot - (cnt - k) * start
```
## Tags

* [Stack](/Collections/stack.md#stack) > [Monotonic stack](/Collections/stack.md#monotonic-stack)
* [Binary search](/Collections/binary-search.md#binary-search)
* [Two pointers](/Collections/two-pointers.md#two-pointers)
* [Prefix](/Collections/prefix.md#prefix) > [Sum](/Collections/prefix.md#sum)
