# https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counts = sorted(Counter(arr).values())
        ret, i = len(counts), 0
        for count in counts:
            if k >= count:
                k -= count
                ret -= 1
            else:
                break
        return ret
