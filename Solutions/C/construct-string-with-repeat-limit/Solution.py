# https://leetcode.com/problems/construct-string-with-repeat-limit/

class Solution:
    def repeatLimitedString(self, s: str, limit: int) -> str:
        ctr = sorted(list(map(list, Counter(s).items())))
        ret = ''
        while ctr:
            ret += ctr[-1][0] * (add := min(ctr[-1][1], limit))
            if ctr[-1][1] == add:
                ctr.pop(-1)
                continue
            ctr[-1][1] -= add
            if len(ctr) == 1:
                break
            ret += ctr[-2][0]
            if ctr[-2][1] == 1:
                ctr[-2] = ctr[-1]
                ctr.pop(-1)
            else:
                ctr[-2][1] -= 1
        return ret
