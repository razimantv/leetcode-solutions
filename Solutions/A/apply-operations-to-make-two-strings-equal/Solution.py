# https://leetcode.com/problems/apply-operations-to-make-two-strings-equal/

class Solution:
    def minOperations(self, s1: str, s2: str, x: int) -> int:
        indices = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                indices.append(i)

        L = len(indices)
        if L % 2:
            return -1
        elif not L:
            return 0

        dp = [[0]*L for i in range(L)]
        for i in range(1, L):
            dp[i-1][i] = min(x, indices[i]-indices[i-1])

        for l in range(3, L, 2):
            for j in range(l, L):
                i = j - l
                dp[i][j] = min(x, indices[j]-indices[i]) + dp[i+1][j-1]
                for k in range(i+1, j, 2):
                    dp[i][j] = min(dp[i][j], min(
                        x, indices[k]-indices[i]) + dp[i+1][k-1] + dp[k+1][j])
        return dp[0][L-1]
