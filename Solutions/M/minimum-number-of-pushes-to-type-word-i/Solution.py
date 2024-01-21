# https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-i/

class Solution:
    def minimumPushes(self, word: str) -> int:
        return sum(
            (i // 8 + 1) * x for i, x in enumerate(
                sorted(Counter(word).values(), reverse=True)
            )
        )
