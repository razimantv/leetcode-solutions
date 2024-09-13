# https://leetcode.com/problems/xor-queries-of-a-subarray/

class Solution:
    def xorQueries(
        self, arr: List[int], queries: List[List[int]]
    ) -> List[int]:
        xarr = [0] + list(accumulate(arr, xor))
        return [xarr[r + 1] ^ xarr[l] for l, r in queries]
