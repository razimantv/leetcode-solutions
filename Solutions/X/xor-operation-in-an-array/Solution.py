# https://leetcode.com/problems/xor-operation-in-an-array


class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        if n == 1:
            return start
        end = start + 2 * (n - 1)
        ret = 0
        if start % 4 > 1:
            ret ^= start
            n -= 1
        if end % 4 < 2:
            ret ^= end
            n -= 1
        if n % 4 == 2:
            ret ^= 2
        return ret
