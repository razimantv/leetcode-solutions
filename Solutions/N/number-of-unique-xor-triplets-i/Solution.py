# https://leetcode.com/problems/number-of-unique-xor-triplets-i

class Solution:
    def uniqueXorTriplets(self, nums: list[int]) -> int:
        n, ret = max(nums), 1
        if n < 3:
            return n
        while ret <= n:
            ret <<= 1
        return ret
