# https://leetcode.com/problems/convert-1d-array-into-2d-array

class Solution:
    def construct2DArray(
        self, original: List[int], m: int, n: int
    ) -> List[List[int]]:
        return [
            original[i * n:(i + 1) * n] for i in range(m)
        ] if m * n == len(original) else []
