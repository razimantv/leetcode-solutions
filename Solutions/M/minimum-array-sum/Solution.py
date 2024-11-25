# https://leetcode.com/problems/minimum-array-sum/

class Solution:
    def minArraySum(self, nums: List[int], k: int, op1: int, op2: int) -> int:
        dp = [[0] * (op2 + 1) for _ in range(op1 + 1)]
        for x in nums:
            newdp = [[x + y for y in row] for row in dp]
            for i in range(op1 + 1):
                for j in range(op2 + 1):
                    if i < op1:
                        newdp[i+1][j] = min(
                            newdp[i+1][j], dp[i][j] + (x + 1) // 2
                        )
                    if j < op2 and x >= k:
                        newdp[i][j + 1] = min(
                            newdp[i][j + 1], dp[i][j] + x - k
                        )
                        if i < op1:
                            newdp[i + 1][j + 1] = min(
                                newdp[i + 1][j + 1],
                                dp[i][j] + (x - k + 1) // 2
                            )
                    if i < op1 and j < op2 and (x + 1) // 2 >= k:
                        newdp[i + 1][j + 1] = min(
                            newdp[i + 1][j + 1], dp[i][j] + (x + 1) // 2 - k
                        )
            dp = newdp
        return min(min(row for row in dp))
