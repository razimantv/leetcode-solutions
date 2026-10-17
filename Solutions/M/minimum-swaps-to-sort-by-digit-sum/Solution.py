# https://leetcode.com/problems/minimum-swaps-to-sort-by-digit-sum/


class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        def digsum(x):
            return sum(map(int, str(x)))

        posmap = {
            x: i for i, (_, x) in enumerate(sorted(
                [(digsum(x), x) for x in nums]
            ))
        }
        nums = [posmap[x] for x in nums]

        ret = len(nums)
        for i in range(len(nums)):
            if nums[i] == -1:
                continue
            j = i
            while nums[j] != -1:
                jj = nums[j]
                nums[j] = -1
                j = jj
            ret -= 1
        return ret
