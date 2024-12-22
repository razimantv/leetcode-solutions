# https://leetcode.com/problems/minimum-number-of-operations-to-make-elements-in-array-distinct

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        seen = set()
        for x in nums[::-1]:
            if x in seen:
                break
            seen. add(x)
        remove = len(nums) - len(seen)
        return (remove + 2) // 3
