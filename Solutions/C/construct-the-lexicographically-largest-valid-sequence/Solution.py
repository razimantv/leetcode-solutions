# https://leetcode.com/problems/construct-the-lexicographically-largest-valid-sequence/

class Solution:
    def constructDistancedSequence(self, n: int) -> list[int]:
        L = 2 * n - 1
        ret = [0] * L
        used = set()

        def work(i):
            if i == L:
                return True
            if ret[i]:
                return work(i + 1)
            for x in range(n, 0, -1):
                if x in used or (x > 1 and (i + x >= L or ret[i + x])):
                    continue
                used.add(x)
                ret[i] = x
                if x > 1:
                    ret[i + x] = x
                if work(i + 1):
                    return True
                used.remove(x)
                ret[i] = 0
                if x > 1:
                    ret[i + x] = 0
            return False

        work(0)
        return ret
