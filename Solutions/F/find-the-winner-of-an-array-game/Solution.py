# https://leetcode.com/problems/find-the-winner-of-an-array-game/

class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        cnt = 1
        winner = max(arr[0], arr[1])
        if k == 1:
            return winner
        for x in arr[2:]:
            if x > winner:
                winner, cnt = x, 1
            else:
                cnt += 1
                if cnt == k:
                    break
        return winner
