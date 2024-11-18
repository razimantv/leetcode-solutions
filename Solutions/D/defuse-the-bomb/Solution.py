# https://leetcode.com/problems/defuse-the-bomb/

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n, psum = len(code), list(accumulate(code * 3))
        return [
            abs(psum[i + k - (k < 0)] - psum[i - (k < 0)])
            for i in range(n, 2 * n)
        ]
