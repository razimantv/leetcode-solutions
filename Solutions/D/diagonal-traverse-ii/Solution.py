# https://leetcode.com/problems/diagonal-traverse-ii/

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        return [
            x for a, b, x in sorted(
                (i+j, -i, x)
                for i, row in enumerate(nums)
                for j, x in enumerate(row)
            )
        ]
