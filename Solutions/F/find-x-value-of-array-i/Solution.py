# https://leetcode.com/problems/find-x-value-of-array-i/

class Solution:
    def resultArray(self, nums: list[int], k: int) -> list[int]:
        old, ret = [[0] * k for _ in range(2)]
        for x in nums:
            new = [0] * k
            x %= k
            new[x] += 1
            ret[x] += 1
            for i in range(k):
                xi = (x * i) % k
                new[xi] += old[i]
                ret[xi] += old[i]
            old = new
        return ret
