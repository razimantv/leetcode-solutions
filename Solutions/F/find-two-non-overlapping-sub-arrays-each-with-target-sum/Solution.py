# https://leetcode.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/

class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        best, prev, ret = [], inf, inf
        l, window = 0, 0
        for r in range(n):
            cur = prev
            window += arr[r]
            while window > target:
                window -= arr[l]
                l += 1
            if window == target:
                cur = r - l + 1
                if l:
                    ret = min(ret, cur + best[l - 1])
                cur = min(cur, prev)
                prev = cur
            best.append(cur)
        return -1 if ret > n else ret
