# https://leetcode.com/problems/greatest-sum-divisible-by-three/

class Solution:
    def maxSumDivThree(self, nums: list[int]) -> int:
        byrem, tot = defaultdict(list), sum(nums)
        if not (rem := tot % 3):
            return tot
        for x in nums:
            if (r := x % 3):
                byrem[r]. append(x)
        sub = math. inf
        for k in byrem:
            byrem[k] = sorted(byrem[k])[:2]
        if byrem[rem]:
            sub = byrem[rem][0]
        if len(byrem[rem2 := 3 - rem]) == 2:
            sub = min(sub, sum(byrem[rem2]))
        return tot - sub
