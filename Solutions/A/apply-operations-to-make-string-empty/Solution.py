# https://leetcode.com/problems/apply-operations-to-make-string-empty/

class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        ctr = Counter(s)
        maxct = max(ctr.values())

        last = {}
        for i, x in enumerate(s):
            last[x] = i
        return ''.join(sorted(
            [c for c, v in ctr.items() if v == maxct],
            key=lambda x: last[x]
        ))
