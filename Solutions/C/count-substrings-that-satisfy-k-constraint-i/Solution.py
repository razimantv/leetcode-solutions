# https://leetcode.com/problems/count-substrings-that-satisfy-k-constraint-i/

class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        n, ret = len(s), 0
        for i in range(n):
            zero, one = 0, 0
            for j in range(i, n):
                if s[j] == '0':
                    zero += 1
                else:
                    one += 1
                if min(zero, one) > k:
                    break
                ret += 1
        return ret
