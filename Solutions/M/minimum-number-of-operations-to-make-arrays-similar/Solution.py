# https://leetcode.com/problems/minimum-number-of-operations-to-make-arrays-similar/

class Solution:
    def oddeven(self, nums):
        odd = sorted(filter(lambda x: x % 2 == 1, nums))
        even = sorted(filter(lambda x: x % 2 == 0, nums))
        return odd, even

    def work(self, v1, v2):
        n = len(v1)
        return sum([v1[i]-v2[i] for i in range(n) if v1[i] > v2[i]]) // 2

    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        odd1, even1 = self.oddeven(nums)
        odd2, even2 = self.oddeven(target)
        return self.work(odd1, odd2) + self.work(even1, even2)
