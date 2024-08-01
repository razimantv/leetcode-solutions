# Earliest second to mark indices ii

[Problem link](https://leetcode.com/problems/earliest-second-to-mark-indices-ii/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/earliest-second-to-mark-indices-ii/

class Solution:
    def earliestSecondToMarkIndices(
        self, nums: List[int], indices: List[int]
    ) -> int:
        n, m, tot = len(nums), len(indices), sum(nums)
        first = {}
        for i, x in enumerate(indices):
            if nums[x-1] and x not in first:
                first[x] = i
        isfirst = set(first.values())

        def work(k):
            free, pq, rem, remtot = 0, [], 0, 0
            for i in range(k - 1, -1, -1):
                if i not in isfirst:
                    free += 1
                    continue
                x = nums[indices[i] - 1]
                rem += 1
                remtot += x
                heappush(pq, x)
                if free:
                    free -= 1
                else:
                    free += 1
                    rem -= 1
                    remtot -= heappop(pq)
            return free >= tot - remtot + n - rem

        start, end = 0, m + 1
        while end - start > 1:
            mid = (end + start) // 2
            if work(mid):
                end = mid
            else:
                start = mid
        return -1 if end > m else end
```
## Tags

* [Binary search](/Collections/binary-search.md#binary-search)
* [Greedy](/Collections/greedy.md#greedy)
* [Priority queue](/Collections/priority-queue.md#priority-queue)
