# https://leetcode.com/problems/lexicographical-numbers/

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ret = []

        def work(x):
            for y in range(max(1, 10 * x), min(n, 10 * x + 9) + 1):
                ret.append(y)
                work(y)
        work(0)
        return ret
