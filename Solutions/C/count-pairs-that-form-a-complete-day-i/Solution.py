# https://leetcode.com/problems/count-pairs-that-form-a-complete-day-i/

class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        cnt = defaultdict(int)
        ret = 0
        for x in hours:
            ret += cnt[(24 - x % 24) % 24]
            cnt[x % 24] += 1
        return ret
