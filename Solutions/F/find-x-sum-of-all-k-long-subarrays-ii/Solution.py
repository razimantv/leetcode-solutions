# https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-ii/

from sortedcontainers import SortedList


class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        rest = SortedList()
        cnt = Counter(nums[:k])
        top = SortedList((v, k) for k, v in cnt.items())
        while len(top) > x:
            rest.add(top.pop(0))
        tot = sum(k * v for v, k in top)
        ret = [tot]

        def remove(cnt, val):
            nonlocal tot
            if cnt:
                if (cnt, val) in top:
                    top.remove((cnt, val))
                    tot -= cnt * val
                else:
                    rest.remove((cnt, val))

        def change(y, delta):
            remove(cnt[y], y)
            cnt[y] += delta
            if cnt[y]:
                rest.add((cnt[y], y))

        for i in range(k, len(nums)):
            change(nums[i], 1)
            change(nums[i - k], -1)
            while rest and (len(top) < x or top[0] < rest[-1]):
                tot += rest[-1][0] * rest[-1][1]
                top. add(rest.pop(-1))
                if len(top) > x:
                    tot -= top[0][0] * top[0][1]
                    rest.add(top.pop(0))
            ret.append(tot)
        return ret
