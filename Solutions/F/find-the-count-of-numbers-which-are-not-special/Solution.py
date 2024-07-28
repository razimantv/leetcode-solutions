# https://leetcode.com/problems/find-the-count-of-numbers-which-are-not-special/

class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        notprime = [0] * 31623
        cnt = notprime
        for i in range(2, 31623):
            if not notprime[i]:
                for j in range(i * i, 31623, i):
                    notprime[j] = 1
            cnt[i] = cnt[i - 1] + 1 - notprime[i]  # Haha

        return r - l + 1 - (
            cnt[int(math.sqrt(r))] - cnt[int(math.sqrt(l - 1))]
        )
