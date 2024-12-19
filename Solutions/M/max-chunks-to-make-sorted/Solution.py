# https://leetcode.com/problems/max-chunks-to-make-sorted/

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        l, L, R, ret = 0, arr[0], arr[0], 1
        for r, x in enumerate(arr[:-1]):
            L, R = min(L, x), max(R, x)
            if l == L and r == R:
                ret += 1
                L, R = [arr[l := r + 1]] * 2
        return ret
