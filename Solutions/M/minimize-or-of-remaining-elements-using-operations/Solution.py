# https://leetcode.com/problems/minimize-or-of-remaining-elements-using-operations/

class Solution:
    def minOrAfterOperations(self, nums: List[int], k: int) -> int:
        def work(mask):
            # What is the minimum number of pieces array can be split
            # if each piece has bitwise and 0 for mask
            cur, cnt = mask, 0
            for x in nums:
                cur &= x
                if not cur:
                    cnt, cur = cnt + 1, mask
            return cnt

        n, best, inv = len(nums), 0, 0
        for b in range(29, -1, -1):
            inv ^= 1 << b
            if work(inv) + k < n:
                best ^= 1 << b
                inv ^= 1 << b
        return best
