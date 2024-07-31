# https://leetcode.com/problems/filling-bookcase-shelves/

class Solution:
    def minHeightShelves(self, books: List[List[int]], width: int) -> int:
        n = len(books)
        dp = [0]
        for i in range(n):
            curw, curh, cur = 0, 0, 1 << 30
            for j in range(i, -1, -1):
                curw += books[j][0]
                if curw > width:
                    break
                curh = max(curh, books[j][1])
                cur = min(cur, curh + dp[j])
            dp.append(cur)
        return dp[-1]
