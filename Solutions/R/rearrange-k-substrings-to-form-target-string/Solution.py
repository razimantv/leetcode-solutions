# https://leetcode.com/problems/rearrange-k-substrings-to-form-target-string/

class Solution:
    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:
        n = len(s)
        l = n // k
        ctr = Counter(s[i * l: (i + 1) * l] for i in range(k))
        for i in range(k):
            cur = t[i * l:(i + 1) * l]
            if not ctr[cur]:
                return False
            ctr[cur] -= 1
        return True
