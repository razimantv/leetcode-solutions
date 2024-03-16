# https://leetcode.com/problems/mark-elements-on-array-by-performing-queries/

class Solution:
    def unmarkedSumArray(
        self, nums: List[int], queries: List[List[int]]
    ) -> List[int]:
        next, tot = 0, sum(nums)
        snums = sorted([x, i] for i, x in enumerate(nums))
        n = len(nums)
        marked, ret = [False] * n, []

        for idx, k in queries:
            if not marked[idx]:
                marked[idx] = True
                tot -= nums[idx]
            while k and next < n:
                if not marked[snums[next][1]]:
                    k -= 1
                    marked[snums[next][1]] = True
                    tot -= snums[next][0]
                next += 1
            ret.append(tot)
        return ret
