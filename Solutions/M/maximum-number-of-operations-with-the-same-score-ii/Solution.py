# https://leetcode.com/problems/maximum-number-of-operations-with-the-same-score-ii/

class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        scores = [nums[0] + nums[1], nums[0] + nums[-1], nums[-1] + nums[-2]]
        n = len(nums)
        cache = [[[-1] * n for _ in range(n)] for scoreid in range(3)]

        def work(scoreid, l, r):
            if r <= l:
                return 0
            if cache[scoreid][l][r] == -1:
                cache[scoreid][l][r] = 0
                if nums[l] + nums[l+1] == scores[scoreid]:
                    cache[scoreid][l][r] = max(
                        cache[scoreid][l][r], 1 + work(scoreid, l+2, r)
                    )
                if nums[l] + nums[r] == scores[scoreid]:
                    cache[scoreid][l][r] = max(
                        cache[scoreid][l][r], 1 + work(scoreid, l+1, r-1)
                    )
                if nums[r-1] + nums[r] == scores[scoreid]:
                    cache[scoreid][l][r] = max(
                        cache[scoreid][l][r], 1 + work(scoreid, l, r-2)
                    )
            return cache[scoreid][l][r]

        return max(work(scoreid, 0, n-1) for scoreid in range(3))
