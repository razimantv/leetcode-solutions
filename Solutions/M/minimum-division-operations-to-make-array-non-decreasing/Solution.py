# https://leetcode.com/problems/minimum-division-operations-to-make-array-non-decreasing/

class Solution:
    def __init__(self):
        self.cache = {}

    def convert(self, x):
        if x in self.cache:
            return self.cache[x]
        y = 2
        while y * y <= x:
            if x % y == 0:
                self.cache[x] = y
                return y
            y += 1
        self.cache[x] = x
        return x

    def minOperations(self, nums: List[int]) -> int:
        prev, ret = nums[-1], 0
        for x in nums[-2::-1]:
            if x <= prev:
                prev = x
            elif (y := self.convert(x)) <= prev:
                ret += 1
                prev = y
            else:
                return -1

        return ret
