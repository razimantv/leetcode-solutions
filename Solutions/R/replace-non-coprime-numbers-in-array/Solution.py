# https://leetcode.com/problems/replace-non-coprime-numbers-in-array/

class Solution:
    def replaceNonCoprimes(self, nums: list[int]) -> list[int]:
        ret = []
        for x in nums:
            ret. append(x)
            while len(ret) > 1 and (g := gcd(ret[-1], ret[-2])) > 1:
                x = ret.pop()
                y = ret.pop()
                ret. append(x * y // g)
        return ret
