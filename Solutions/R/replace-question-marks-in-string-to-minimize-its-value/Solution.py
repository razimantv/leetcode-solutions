# https://leetcode.com/problems/replace-question-marks-in-string-to-minimize-its-value/

class Solution:
    def minimizeStringValue(self, s: str) -> str:
        n = len(s)
        ctr = Counter(c for c in s if c != '?')
        vals = sorted(ctr.values())
        zero, qct = 26 - len(vals), n - sum(vals)

        sub = 0
        for i, x in enumerate(vals):
            if (zero + i) * x - sub > qct:
                x1 = (qct + sub) % (zero + i)
                x2 = zero + i - x1
                y2 = (qct + sub) // (zero + i)
                y1 = y2 + (1 if x2 else 0)
                break
            else:
                sub += x
        else:
            x1 = n % 26
            x2 = 26 - x1
            y2 = n // 26
            y1 = y2 + (1 if x2 else 0)

        ret, next = '', 'a'
        for c in s:
            if c != '?':
                ret += c
                continue
            while (x1 and ctr[next] >= y1) or (not x1 and ctr[next] >= y2):
                next = chr(ord(next) + 1)
            ret += next
            ctr[next] += 1
            if ctr[next] == y1:
                x1 -= 1

        return ret
