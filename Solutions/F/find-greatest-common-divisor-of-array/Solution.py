# https://leetcode.com/problems/find-greatest-common-divisor-of-array/

class Solution:
    def findGCD(self, nums: list[int]) -> int:
        return gcd(min(nums), max(nums))
