# https://leetcode.com/problems/find-mirror-score-of-a-string

class Solution:
    def calculateScore(self, s: str) -> int:
        pos = defaultdict(list)
        rev = {
            c: d for c, d in zip(
                string.ascii_lowercase, string.ascii_lowercase[::-1]
            )
        }
        
        ret = 0
        for i, c in enumerate(s):
            if not pos[rev[c]]:
                pos[c].append(i)
            else:
                ret += i - pos[rev[c]].pop()
        return ret
