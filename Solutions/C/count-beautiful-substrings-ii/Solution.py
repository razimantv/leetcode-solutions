# https://leetcode.com/problems/count-beautiful-substrings-ii/

class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        vowels = "aeiou"
        v, c = 0, 0
        lists = defaultdict(lambda: defaultdict(int))
        lists[0][0] = 1
        for x in s:
            if x in vowels:
                v += 1
            else:
                c += 1
            lists[v - c][v % k] += 1

        ret = 0
        for key, v in lists.items():
            cur = list(v.items())
            n = len(cur)
            for i in range(n):
                x1, y1 = cur[i]
                ret += y1 * (y1-1) // 2
                for j in range(i):
                    x2, y2 = cur[j]
                    if (x1 - x2) ** 2 % k == 0:
                        ret += y1 * y2
        return ret
