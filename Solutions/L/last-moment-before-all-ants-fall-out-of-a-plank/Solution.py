# https://leetcode.com/problems/last-moment-before-all-ants-fall-out-of-a-plank/

class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        ret = 0
        if left:
            ret = max(ret, max(left))
        if right:
            ret = max(ret, n-min(right))
        return ret
