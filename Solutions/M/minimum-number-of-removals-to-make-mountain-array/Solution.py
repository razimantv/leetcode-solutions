# https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/

class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        def lis(ar):
            order, ret = [], []
            for x in ar:
                pos = bisect_left(order, x)
                ret.append(pos + 1)
                if pos == len(order):
                    order.append(0)
                order[pos] = x
            return ret

        left, right = lis(nums), lis(nums[::-1])[::-1]
        return len(nums) - max(
            x + y - 1 for x, y in zip(left, right) if min(x, y) > 1
        )
