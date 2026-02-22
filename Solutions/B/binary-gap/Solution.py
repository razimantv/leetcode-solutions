# https://leetcode.com/problems/binary-gap/

class Solution:
    def binaryGap(self, n: int) -> int:
        return max(
            (
                y - x for x, y in pairwise(
                    i for i, c in enumerate(f'{n:b}') if c == '1'
                )
            ),
            default=0
        )
