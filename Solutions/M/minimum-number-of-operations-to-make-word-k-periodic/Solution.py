# https://leetcode.com/problems/minimum-number-of-operations-to-make-word-k-periodic/

class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        n = len(word)
        cnt = Counter(word[i:i+k] for i in range(0, n, k))
        return n // k - max(cnt.values())
