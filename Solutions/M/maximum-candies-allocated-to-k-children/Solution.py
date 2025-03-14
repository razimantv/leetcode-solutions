# https://leetcode.com/problems/maximum-candies-allocated-to-k-children/

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        start, end = 0, max(candies) + 1
        while end - start > 1:
            mid = (start + end) // 2
            if sum(x // mid for x in candies) >= k:
                start = mid
            else:
                end = mid
        return start
