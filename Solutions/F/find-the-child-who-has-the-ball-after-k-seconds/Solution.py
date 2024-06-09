# https://leetcode.com/problems/find-the-child-who-has-the-ball-after-k-seconds/

class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        k1, k2 = (k // (n - 1)) & 1, k % (n - 1)
        return n - 1 - k2 if k1 else k2
