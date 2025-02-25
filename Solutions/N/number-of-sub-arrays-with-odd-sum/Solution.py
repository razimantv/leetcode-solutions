# https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/

class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        ctr = Counter(x & 1 for x in list(accumulate(arr)))
        return ((ctr[0] + 1) * ctr[1]) % (10 ** 9 + 7)
