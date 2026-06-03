# https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-ii/

class Solution:
    def earliestFinishTime(
        self, landT: list[int], landD: list[int],
        waterT: list[int], waterD: list[int]
    ) -> int:
        def work(a, b):
            t1 = min(x + y for x, y in a)
            return min(max(x, t1) + y for x, y in b)

        return min(
            work(zip(landT, landD), zip(waterT, waterD)),
            work(zip(waterT, waterD), zip(landT, landD))
        )
