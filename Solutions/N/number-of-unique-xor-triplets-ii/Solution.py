# https://leetcode.com/problems/number-of-unique-xor-triplets-ii

class Solution:
    def uniqueXorTriplets(self, nums: list[int]) -> int:
        xors = [{0: 1}] + [{} for _ in range(3)]
        
        for x in nums:
            for i in range(3):
                for y in xors[i]:
                    xors[i + 1][x ^ y] = 1
        return len(xors[3])
