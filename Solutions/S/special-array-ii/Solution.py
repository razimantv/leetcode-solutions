# https://leetcode.com/problems/special-array-ii/

class Solution:
    def isArraySpecial(
        self, nums: List[int], queries: List[List[int]]
    ) -> List[bool]:
        n = len(nums)
        last = [-1]
        for i in range(1, n):
            last.append(
                last[-1] if (nums[i] + nums [i - 1]) & 1 else i - 1
            )
        
        return [last[r] < l for l, r in queries]
