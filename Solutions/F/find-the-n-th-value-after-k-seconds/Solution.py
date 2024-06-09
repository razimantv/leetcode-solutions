# https://leetcode.com/problems/find-the-n-th-value-after-k-seconds/

class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        ar = [1] * n
        for i in range(k):
            for j in range(1, n):
                ar[j] = (ar[j] + ar[j-1]) % (10 ** 9 + 7)
        return ar[-1]
