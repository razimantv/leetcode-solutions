# https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-ii/

class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        n, ret, cnt = len(s), -math.inf, {
            c: [0] + list(accumulate(1 if sc == c else 0 for sc in s))
            for c in '01234'
        }
        for c in '01234':
            for d in '01234':
                if c == d:
                    continue
                cc, cd, l = cnt[c], cnt[d], 0
                parity = [[math.inf] * 2 for _ in (0, 1)]
                for r in range(k, n + 1):
                    while r - l >= k and cc[r] > cc[l] and cd[r] > cd[l]:
                        parity[cc[l] & 1][cd[l] & 1] = min(
                            parity[cc[l] & 1][cd[l] & 1], cc[l] - cd[l]
                        )
                        l += 1
                    ret = max(
                        ret,
                        cc[r] - cd[r] - parity[(cc[r] & 1) ^ 1][cd[r] & 1]
                    )
        return ret
