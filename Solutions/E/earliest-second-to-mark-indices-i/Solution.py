# https://leetcode.com/problems/earliest-second-to-mark-indices-i/

class Solution:
    def earliestSecondToMarkIndices(self, nums: List[int], indices: List[int]) -> int:
        n, m = len(nums), len(indices)

        def work(k):
            todo, rem = set(range(n)), 0
            for i in range(k - 1, -1, -1):
                x = indices[i] - 1
                if x in todo:
                    rem += nums[x]
                    todo.remove(x)
                elif rem:
                    rem -= 1

            return not todo and not rem

        start, end = n - 1, m + 1
        while end - start > 1:
            mid = (start + end) // 2
            if work(mid):
                end = mid
            else:
                start = mid

        return -1 if end > m else end
