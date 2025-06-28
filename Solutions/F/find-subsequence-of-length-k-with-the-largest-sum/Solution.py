# https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/

class Solution:
    def maxSubsequence(self, nums: list[int], k: int) -> list[int]:
        ctr = sorted(list(Counter(nums).items()), reverse=True)
        used = 0
        for x, c in ctr:
            if used + c >= k:
                mid, midc = x, k - used
                break
            used += c

        ret = []
        for x in nums:
            if x > mid:
                ret.append(x)
            elif x == mid and midc:
                ret.append(x)
                midc -= 1
        return ret
