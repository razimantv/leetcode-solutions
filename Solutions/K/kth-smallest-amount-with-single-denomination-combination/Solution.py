# https://leetcode.com/problems/kth-smallest-amount-with-single-denomination-combination/

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        val, sign = [1], [-1]
        for x in coins:
            newval, newsign = [], []
            for y, s in zip(val, sign):
                newval.append(math.lcm(x, y))
                newsign.append(-s)
            val += newval
            sign += newsign
        val, sign = val[1:], sign[1:]

        def cnt(n):
            return sum(n // x * s for x, s in zip(val, sign))

        start, end = 0, k * min(coins)
        while end - start > 1:
            mid = (start + end) // 2
            if cnt(mid) < k:
                start = mid
            else:
                end = mid

        return end
