# https://leetcode.com/problems/next-greater-numerically-balanced-number/

class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        while True:
            n += 1
            for k, v in Counter(str(n)).items():
                if int(k) != v:
                    break
            else:
                return n
