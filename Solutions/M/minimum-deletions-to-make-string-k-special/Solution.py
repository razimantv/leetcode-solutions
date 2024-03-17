# https://leetcode.com/problems/minimum-deletions-to-make-string-k-special/

class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        counts = Counter(word).values()
        best = len(word)
        for x in counts:
            cur = 0
            for y in counts:
                if y < x:
                    cur += y
                elif y > x + k:
                    cur += y - x - k
            best = min(best, cur)
        return best
