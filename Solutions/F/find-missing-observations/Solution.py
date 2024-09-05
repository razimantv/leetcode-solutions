# https://leetcode.com/problems/find-missing-observations/

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        total = mean * (len(rolls) + n) - sum(rolls)
        if not (n <= total <= 6 * n):
            return []
        return [total // n + 1] * (total % n) + [total // n] * (n - total % n)
