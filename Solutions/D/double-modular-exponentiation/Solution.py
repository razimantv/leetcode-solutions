# https://leetcode.com/problems/double-modular-exponentiation/

class Solution:
    def getGoodIndices(
        self, variables: List[List[int]], target: int
    ) -> List[int]:
        def modpow(a, n, m):
            ret = 1
            while n:
                if n & 1:
                    ret = (ret * a) % m
                a = (a * a) % m
                n >>= 1
            return ret

        return [
            i for i, (a, b, c, d) in enumerate(variables)
            if modpow(modpow(a, b, 10), c, d) == target
        ]
