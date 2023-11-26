# https://leetcode.com/problems/make-lexicographically-smallest-array-by-swapping-elements/

class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        pairs = sorted([(x, i) for i, x in enumerate(nums)])
        n = len(nums)
        l = 0
        while l < n:
            r = l + 1
            while r < n and pairs[r][0] - pairs[r-1][0] <= limit:
                r += 1
            indices = sorted([i for x, i in pairs[l:r]])
            for i, (x, i0) in zip(indices, pairs[l:r]):
                nums[i] = x
            l = r
        return nums
