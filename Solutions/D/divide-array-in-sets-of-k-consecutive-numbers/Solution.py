# https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/

from sortedcontainers import SortedList


class Solution:
    def isPossibleDivide(self, nums: List[int], group: int) -> bool:
        sl = SortedList(map(list, Counter(nums).items()))

        while sl:
            x, cnt = sl.pop()
            if not cnt:
                continue
            elif len(sl) < group - 1:
                return False
            for i in range(1, group):
                if sl[-i] < [x - i, cnt]:
                    return False
                sl[-i][1] -= cnt
        return True
