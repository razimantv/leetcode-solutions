# https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-consonants-ii/

class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        n = len(word)
        cnt, ret = defaultdict(int), 0
        m, r, k1, k2 = 0, 0, 0, 0
        for l, c in enumerate(word):
            while m < n and (
                    any(x for x in 'aeiou' if x not in cnt) or k1 < k
            ):
                if word[m] in 'aeiou':
                    cnt[word[m]] += 1
                else:
                    k1 += 1
                m += 1
            while r < n and (r < m or k2 <= k):
                if word[r] not in 'aeiou':
                    k2 += 1
                r += 1
            ret += r - m
            if r == n and k2 == k and not [x for x in 'aeiou' if x not in cnt]:
                ret += 1
            if c in 'aeiou':
                cnt[c] -= 1
                if not cnt[c]:
                    del cnt[c]
            else:
                k1, k2 = k1 - 1, k2 - 1
        return ret
