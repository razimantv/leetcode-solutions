# https://leetcode.com/problems/binary-prefix-divisible-by-5/

class Solution:
    def prefixesDivBy5(self, nums: list[int]) -> list[bool]:
        ret, cur = [], 0
        for x in nums:
            ret. append(not (cur := (cur * 2 + x) % 5))

        return ret
