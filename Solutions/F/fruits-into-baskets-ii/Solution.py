# https://leetcode.com/problems/fruits-into-baskets-ii/

class Solution:
    def numOfUnplacedFruits(
        self, fruits: list[int], baskets: list[int]
    ) -> int:
        ret, n = 0, len(baskets)
        for x in fruits:
            for i in range(n):
                if baskets[i] >= x:
                    baskets[i] = 0
                    break
            else:
                ret += 1
        return ret
