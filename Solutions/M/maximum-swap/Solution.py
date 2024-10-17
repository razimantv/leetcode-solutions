# https://leetcode.com/problems/maximum-swap/

class Solution:
    def maximumSwap(self, num: int) -> int:
        num = str(num)
        snum = sorted(num, reverse=True)
        for i, (c, d) in enumerate(zip(num, snum)):
            if c != d:
                break
        else:
            return int(num)

        for j in range(len(num) - 1, -1, -1):
            if num[j] == d:
                break
        return int(num[:i] + d + num[i+1:j] + c + num[j+1:])
