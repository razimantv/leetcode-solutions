# https://leetcode.com/problems/build-an-array-with-stack-operations/

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ret = []
        next = 1
        for x in target:
            for y in range(next, x):
                ret += ["Push", "Pop"]
            ret.append("Push")
            next = x + 1
        return ret
